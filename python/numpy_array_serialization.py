import io
import re
import json
import numpy as np
from base64 import b64decode, b64encode

from typing import Tuple, Dict


INIT_TAG = "<data>"
END_TAG = "</data>"

def _Decode(stdout: bytes, keys: Tuple[str, ...]) -> Dict[str, np.ndarray]:

    m = re.search(f"{INIT_TAG}(.*){END_TAG}", stdout.decode(), re.DOTALL)
    if m is None:
        raise IOError("Couldn't decode string - markup not found")
    raw_output = m.group(1)
    b64_code = raw_output.strip("'")
    decoded = json.loads(b64decode(b64_code))

    def _EncodeStringWithBackSlashes(text: str) -> bytes:
        encoded = text.encode().decode("unicode_escape").encode("raw_unicode_escape")
        return encoded

    def _DecompressArray(array: str) -> np.ndarray:
        # remove b'...' chars from encoded string
        memfile = io.BytesIO(_EncodeStringWithBackSlashes(array)[2:-1])
        zipped = np.load(memfile, allow_pickle=True)
        return zipped['arr_0']

    for key in keys:
        decoded[key] = _DecompressArray(decoded[key])

    return decoded

def _Encode(stdin: bytes, keys: Tuple[str, ...]) -> str:

    def CompressArray(array: np.ndarray) -> bytes:
        memfile = io.BytesIO()
        np.savez_compressed(memfile, array)
        memfile.seek(0)
        return memfile.read()
    
    for key in keys:
        stdin[key] = str(CompressArray(stdin[key]))

    serialized_list = [stdin] # converting to list here, change if necessary
    encoded_result = b64encode(json.dumps(serialized_list).encode())
    encoded_result = str(encoded_result)[2:-1] # remove b'...' chars

    def _AddOutputTags(text: str) -> str:
        return INIT_TAG + text + END_TAG

    return _AddOutputTags(encoded_result)

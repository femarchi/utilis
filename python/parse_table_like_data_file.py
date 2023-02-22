from collections import deque
from typing import Any, BinaryIO, Callable, Dict, List


def parse(
    file: BinaryIO,
    column_converter_map: Dict[str, Callable[[str], Any]],
    *,
    encoding: str='utf-8',
    field_separator: str='\t',
) -> List[List[Any]]:
    """
    Parse byte table to list and convert to correct types based on the given map
    """
    data: str = file.read().decode(encoding)

    CRLF = '\r\n' # newline for windows
    lines = deque(data.split('\n') if not CRLF in data else data.split(CRLF))

    column_headers = lines.popleft().split(field_separator)

    result = []
    while lines:
        fields = [
            field.strip(' ').replace(',', '.')
            for field in lines.popleft().split(field_separator)
        ]
        result.append(
            [
                column_converter_map[header](field)
                for header, field in zip(column_headers, fields)
            ]
        )

    return result

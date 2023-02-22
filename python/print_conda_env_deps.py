import subprocess
import json

output = subprocess.check_output(['conda', 'list', '--export', '--json'])

info_dicts = json.loads(output)
print(f'# total dependencies: {len(info_dicts)}')
for info_dict in info_dicts :
    name = info_dict['name']
    version = info_dict['version']
    channel = info_dict['channel']
    if channel == "pypi":
        # Exclude packages that come from pypi.
        continue
    print(f'- {channel}::{name} =={version}')

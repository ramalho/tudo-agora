"""Add continent information to country flag metadata"""

import os
import json

print('<html><head><title>Countries</title></head><body><table>')
for dirpath, dirnames, filenames in os.walk('flags'):
    for filename in filenames:
        if filename == 'metadata.json':
            with open(os.path.join(dirpath, filename)) as fp:
                metadata = json.load(fp)
                fmt = '<tr><td><a href="{iso_cc}">{iso_cc}</a></td><td>{country}</td></tr>'
                print(fmt.format(**metadata, dirpath=dirpath))
print('</table></body></html>')

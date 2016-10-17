"""Add continent information to country flag metadata"""

import os
import json

index = []

for dirpath, dirnames, filenames in sorted(os.walk('flags')):
    for filename in filenames:
        if filename == 'metadata.json':
            with open(os.path.join(dirpath, filename)) as fp:
                metadata = json.load(fp)
                entry = {'iso_cc': metadata['iso_cc'], 'country': metadata['country']}
                index.append(entry)
print(json.dumps(index, indent=2))

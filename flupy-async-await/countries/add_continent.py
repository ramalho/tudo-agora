"""Add continent information to country flag metadata"""

import os
import json

continents = {}
with open('continents.txt', encoding='utf-8') as fp:
    for continent, country in (
            lin.strip().split(maxsplit=1) for lin in fp):
        continents[country] = continent

for dirpath, dirnames, filenames in os.walk('flags'):
    for filename in filenames:
        if filename == 'metadata.json':
            with open(os.path.join(dirpath, filename)) as fp:
                metadata = json.load(fp)
                country = metadata['country']
                try:
                    metadata['continent'] = continents[country]
                except KeyError:
                    print('Missing:', dirpath, ':', country)
                    continue
            with open(os.path.join(dirpath, filename), 'wt', encoding='utf-8') as fp:
                json.dump(metadata, fp)

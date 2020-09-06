import json
from pprint import pprint

with open("newsafr.json", encoding='utf-8') as f:
    json_data = json.load(f)
    pprint(json_data)
import json
from pathlib import Path
#from pprint import pprint

p = Path("data2.json")
content = p.read_text(encoding='utf8')
data = json.loads(content)

#pprint(data)
print("innehåll:                          100g")
for elem in data:
    if elem['rightalign']:
        print(f"{elem['what']:>25} {elem['value']:12}{elem['unit']}")
    elif not elem['rightalign']:
        print(f"{elem['what']:<25} {elem['value']:12}{elem['unit']}")
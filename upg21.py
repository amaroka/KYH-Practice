from pathlib import Path
import json
p = Path("data1.json").read_text()
data = json.loads(p)

total_lista = []
for item in data['entries']:
    total_lista.append(item['total'])

print(sum(total_lista))
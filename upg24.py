#from pprint import pprint
import requests

URL = "https://proagile.se/api/publicEvents"
r = requests.get(url= URL)

data = r.json()

# today = datetime.datetime.today()

for elements in data:
    print(f"Kursnamn:    {elements['name']}")
    print(f"Startdatum:{elements['startDate']:>12}")
    print(f"Slutdatum:{elements['endDate']:>13}")




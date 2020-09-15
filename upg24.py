#from pprint import pprint
import requests

URL = "https://proagile.se/api/publicEvents"
r = requests.get(url= URL)

data = r.json()

for elements in data:
    print(elements['startDate'])

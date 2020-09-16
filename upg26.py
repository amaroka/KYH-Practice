from pprint import pprint
import requests

r = requests.get("http://www.omdbapi.com/", params={"t": "Alien", "apikey": "9f6d550c"})

pprint(r.json())

import requests
#import datetime

URL = "https://proagile.se/api/publicEvents"
r = requests.get(url= URL)

data = r.json()

#today = datetime.datetime.today()

for elements in data:
    if elements["startDate"] == "2020-09-15":
        print(f"Kursnamn:    {elements['name']}")
        print(f"Startdatum:{elements['startDate']:>12}")
        print(f"Slutdatum:{elements['endDate']:>13}")




import requests
import datetime

URL = "https://proagile.se/api/publicEvents"
r = requests.get(url= URL)

data = r.json()

today = datetime.datetime.today()

time = str(today.date())

year = input("Ange ett år: ")
month = input("Ange en månad: ")
day = list(range(1,32))
startdatum = (f"{year}-{month}-01")
slutdatum = (f"{year}-{month}-31")

kursdatum = data["startDate"]
for elements in data:
    if startdatum <= kursdatum and kursdatum <= slutdatum:
        print(f"Kursnamn:    {elements['name']}")
        print(f"Startdatum:{kursdatum['startDate']:>12}")
        print(f"Slutdatum:{elements['endDate']:>13}")




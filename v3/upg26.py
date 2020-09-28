#from pprint import pprint
import requests



film = input("Sök på en film: ")
r = requests.get("http://www.omdbapi.com/", params={"t": film, "apikey": "9f6d550c"})
data = r.json()


#Title Year Director
#Actors
#imdbRating
#Awards
#Runtime
print("*** Resultat från OMDB! ***")
print(f"{data['Title']} ({data['Year']}) regisserades av {data['Director']} ")
print(f"Skådisar: {data['Actors']}")
print(f"IMDB betyg: {data['imdbRating']}")
print(f"Awards: {data['Awards']}")
print(f"Längd: {data['Runtime']}")
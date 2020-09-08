# mobiltelefon = surfplatta, laptop, blueberry
# THL = SIIS, WHO, UN, FFS,
# Finländare = Göteborgare, Skåningar, Danskefan
# Markku = Johan johansson, Kent agent, Dr snuggles, Karl Gustav XVI

import random

def plat():
    plats = ["SIIS", "WHO", "UN", "FFS"]
    return random.choice(plats)
def natt():
    nat = ["Göteborgare", "skåningar", "Danskefan"]
    return random.choice(nat)
def per():
    person = ["Johan Johansson", "Kent Agent", "Dr snuggles", "Karl XVI Gustav"]
    return random.choice(person)

def mobil():
    tech = ["surfplatta", "laptop", "blueberry"]
    return random.choice(tech)

tech = mobil()
plats = plat()
nat = natt()
person = per()

print(f"En app som kan laddas ned till {tech} ska varna {nat} som kommit nära någon som smittats med coronaviruset.")
print(f"Jag tycker att ni i Sverige borde överväga att göra något liknande, säger {person}, generaldirektör för {plats}.")
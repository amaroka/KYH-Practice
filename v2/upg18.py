def main():

    people = {"Fredrik":"0702778511",
    "Olof": "123456789",
    "Lisa":"9999999999",
    "Bodil": "555-666-789"
    }
    print(f"Så här många personer finns: {len(people)}")
    choice = input("1: Slå upp ett nummer:\n2: Redigera/lägg till nummer:\n>> ")
    if choice == "1":
        vem = input(f"Vem vill du ringa?", )

        if vem not in people:
            print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
        else:
            number = people[vem]
            print(f"Numret till {vem} är {number}")
    if choice == "2":
        name = input("Lägg till namn: ")
        number = input("Lägg till nummer: ")
        people[name] = number

if __name__ == '__main__':
    main()
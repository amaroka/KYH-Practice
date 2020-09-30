def main():

    people = {"Fredrik":"0702778511",
    "Olof": "123456789",
    "Lisa":"9999999999",
    "Bodil": "555-666-789"
    }
    print("Så här många personer finns: {:5}".format(len(people)))
    choice = input("1: Slå upp ett nummer:\n2: Redigera/lägg till nummer:\n>> ")
    if choice == "1":
        vem = input(f"Vem vill du ringa?", )

        if vem not in people:
            print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
        else:
            number = people[vem]
            print("Numret till %s är %s" % (vem, number) )
    if choice == "2":
        name = input("Lägg till namn: ")
        number = input("Lägg till nummer: ")
        people[name] = number

if __name__ == '__main__':
    main()
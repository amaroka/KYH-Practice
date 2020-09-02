import random

n = random.randint(1, 50)
print("Jag tänker på ett nummer mellan 1 och 50, Gissa??")
def ask_number():
    return int(input("Din gissning "))


def mainloop():
    Guess = 0

    while True:
        Num = ask_number()
        as_number = int(Num)
        Guess = Guess+1

        if as_number == n:
            print("Korrekt")
            return Guess


        if as_number < n:
            print("Mitt nummer är högre... Gissa igen!")

        if as_number > n:
            print("Mitt nummer är lägre... Gissa igen!")

Guess = mainloop()
print(f"Du gissade så här mycket: {Guess}")
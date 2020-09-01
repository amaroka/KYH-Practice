import random

n = random.randint(1, 50)
print("Jag tänker på ett nummer mellan 1 och 50, Gissa??")
def ask_number(text):
    return int(text)
Num = ask_number(input())
print(str(Num))

def mainloop():
    Guess = 0

    while True:
        text = input("Din gissning")
        as_number = int(text)
        Guess = Guess+1

        if as_number == n:
            print("Korrekt")
            return Guess


        if as_number < n:
            print("Mitt nummer är högre... Gissa igen!")

        if as_number > n:
            print("Mitt nummer är lägre... Gissa igen!")

Guess = mainloop()
print("Du gissade så här mycket: " + str(Guess))
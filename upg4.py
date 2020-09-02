import random

n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1 och 100, Gissa??")

Guess = 0

while True:
    text = input("Din gissning")
    as_number = int(text)
    Guess = Guess+1
    if as_number == n:
            print("Korrekt, du gissade så här mycket = " + str(Guess))
            break

    if as_number < n:
            print("Mitt nummer är högre... Gissa igen!")

    if as_number > n:
            print("Mitt nummer är lägre... Gissa igen!")
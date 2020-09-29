name = input("Skriv in ett namn: ")
age = input("Skriv in ålder: ")

t = (name, age)

def info(t):
    print(t[0])
    print(t[1])
info(t)
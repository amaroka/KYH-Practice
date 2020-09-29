# name = input("Skriv in ett namn: ")
# age = input("Skriv in ålder: ")
#
# t = (name, age)
#
# def info(t):
#     print(t[0])
#     print(t[1])
# info(t)
#

tal1 = input("Skriv in ett tal: ")
tal2 = input("Skriv in ett tal: ")


def tal(a,b):
    (a,b) = (b,a)
    print(a,b)
tal(tal1,tal2)
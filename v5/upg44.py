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

# tal1 = input("Skriv in ett tal: ")
# tal2 = input("Skriv in ett tal: ")
#
#
# def tal(a,b):
#     (a,b) = (b,a)
#     print(a,b)
# tal(tal1,tal2)



T1 = (1,2,3)
L1 = list(T1)
print(L1)
L1.append(4)
T1 = tuple(L1)
print(T1)



def lista(ls):
    return tuple(ls)
ls = [1,2,3]
print(lista(ls))
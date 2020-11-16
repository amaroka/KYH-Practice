#51.1

add_as_lambda = lambda a, b: a + b
print(add_as_lambda(3, 4))

#51.2

def obj(s):
    return s.upper()
print(obj("hejsan"))

#51.3
def join_as_lambda(string,inbetween):
    return inbetween.join(string)
print(join_as_lambda("abcdef", ","))

#51.4
# anna = ("Anna", "Persson", 42)
# lova = ("Lova", "Andersson", 35)
# alex = ("Alex", "Börjesson", 10)
# people = [anna, lova, alex]
# on_surname = sorted(people, key=lambda p: p[1])
# for (first, last, age) in on_surname:
#     print(f"{first} {last} ({age} år)")

#51.5
# anna = ("Anna", "Persson", 42)
# lova = ("Lova", "Andersson", 35)
# alex = ("Alex", "Börjesson", 10)
# people = [anna, lova, alex]
# on_surname = sorted(people, key=lambda p: p[2])
# for (first, last, age) in on_surname:
#     print(f"{first} {last} ({age} år)")

#51.6
# anna = ("Anna", "Persson", 42)
# lova = ("Lova", "Andersson", 35)
# alex = ("Alex", "Börjesson", 10)
# people = [anna, lova, alex]
# #on_surname = sorted(people, key=lambda p: p[1])
# def age_sorter(people):
#     return people[2]
# people.sort(key=age_sorter)
# for (first, last, age) in people:
#     print(f"{first} {last} ({age} år)")

#51.7
class Person():
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

anna = Person("Anna", "Persson", 42)
lova = Person("Lova", "Andersson", 35)
alex = Person("Alex", "Börjesson", 10)
people = [anna, lova, alex]
people.sort()
for p in people:
    print(f"{p.first} {p.last} ({p.age} år)")




    # on_surname = sorted(people, key=lambda p: p[1])
    # for (first, last, age) in on_surname:
    #     print(f"{first} {last} ({age} år)")
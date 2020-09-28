#39.1
# def max(a,b,c):
#     if a > b and a > c:
#         return a
#     if b > a and b > c:
#         return b
#     if c > a and c > b:
#         return c
# value = max(4,8,6)
# print(value)

#39.2
def total():
    numbers = [5,10,15,20]
    count = 0
    for i in numbers:
        count += i
    print(count)

total()
def max(a,b,c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c
value = max(4,8,6)
print(value)

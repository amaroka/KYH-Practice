#39.1
def max(a,b,c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c


#39.2
def total(totala):
    count = 0
    for i in totala:
        count += i
    return count


#39.3
def total1(tot):
    produkt = 1
    for x in tot:
        produkt *= x
    return produkt

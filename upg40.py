def reverse(txt): #40.1
    return txt

txt1 = "12345"[::-1]
reverse(txt1)
print(txt1)

def upper(txt): #40.2
    count = 0
    for char in txt:
        if char.isupper():
            count += 1
    return count

my_string1 = "Hur Många Stora BokStäver Finns Det"
upper(my_string1)
print(upper(my_string1))

def in_range(value, min, max):  #40.3
    if value > min and value < max:
        return True
    else:
        return False
print(in_range(1,3,2))
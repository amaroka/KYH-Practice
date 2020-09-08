m = input("Skriv en valfri mening: ")

def ordantal(text):

    return len(text.split())

count = ordantal(m)

print(f"Antalet ord är: {count}")
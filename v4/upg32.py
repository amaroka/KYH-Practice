string = input("Mata in en textsträng: ").lower().replace(" ", "")
print(f"{len(string)}")

if string == string[::-1]:
    print("Textsträngen är en palindrom")
else:
    print("Textsträngen är inte en palindrom")
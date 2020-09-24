from upg36 import pwstrength
pw = input("Ange lösenord\n>> ")
print(f"Ditt lösernord fick {pwstrength.compute_strength(pw)}")

def compute_strength(pw):
    count = 0
    legit = '#%&+_-'
    if len(pw) > 10:
        count += 1
    if any(char.isalnum() for char in pw) == True:
        count += 1
    for i in pw:
        if i in legit:
            count += 1
            break
    else:
        pass
    return count
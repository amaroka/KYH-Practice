# m = input("Skriv en valfri mening: ")
#
# def ordantal(text):
#
#     return len(text.split())
#
# count = ordantal(m)
#
# print(f"Antalet ord är: {count}")

vokaler = 'aouåeiyäö'
me = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin euismod commodo tortor, sit amet dictum diam porta non. Duis eget lectus mi."


def vow(me, vokaler):

    me = me.casefold()
    count = {}.fromkeys(vokaler, 0)

    for char in me:
        if char in count:
            count[char] += 1
    return count
print(vow(me, vokaler))
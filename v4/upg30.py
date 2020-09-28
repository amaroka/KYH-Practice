#30.1
# svar = input("Skriv in regnr: ")
# print(f"Bokstävsgrupp: {svar[0:3]}\n Siffergrupp: {svar[3:6]}")

#30.2
# num = []
# tal = input("Ange tal med komma emellan: ").split(",")
# for i in tal:
#     num.append(int(i))
# print(f"Första talet: {tal[0]}\nSista talet: {tal[-1]}\nSumman av talen: {sum(num)}")
# print("Talen baklänges",",".join(tal[::-1]))

#31.1
tal = input("Ange tal med komma emellan: ").split(",")
num = [int(i) for i in tal]
print(f"Första talet: {tal[0]}\nSista talet: {tal[-1]}\nSumman av talen: {sum(num)}\nTalen baklänges: {','.join(tal[::-1])}")
print(f"Udda tal:{tal[0:10:2]} \nJämna tal: {tal[1:100:2]}")
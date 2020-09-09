from pathlib import Path
import sys

def main():
    lista = Path("TODO.txt")
    context = lista.read_text(encoding='utf8').splitlines()
    while True:
        select = int(input("Choose what you want to do:\n1: Titta på listan\n2: Lägg till uppgift\n3: Ta bort uppgift\n4: Avbryt program\n>> "))
        if select == 1:
            read(context)
        elif select == 2:
            context.append(add_on())
        elif select == 3:
            context = delete(context)
        elif select == 4:
            lista.write_text(overwrite(context), encoding='utf8')
            sys.exit()
        else:
            print("Icke giltigt, Bara skinka")
        print("..................................")

def read(context):
    num = 0
    for line in context:
        num = num + 1
        print(f"{num}: {line}")

def add_on():
    return input("Add a Task: ")

def delete(context):
    read(context)
    del_num =  int(input("Erase a task by writing the equivalent number: "))
    del context[del_num - 1]
    print(context)
    return context

def overwrite(context):
    return "\n".join(context)

if __name__ == '__main__':
    main()
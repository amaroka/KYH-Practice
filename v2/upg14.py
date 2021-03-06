# uppgift14.py

FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
TECH = ['Surfplatta', 'Mobil', 'Dator']


def run():
    basket = input("Ange items (komma emellan): ").split(',')
    # basket = [
    #     'volvo', 'is', 'an', 'orange', 'apple', 'Surfplatta', 'Dator'
    # ]
    cars = []
    fruits = []
    tech = []
    rest = []
    for item in basket:
        item = item.strip()
        if item in CARS:
            cars.append(item)
        elif item in FRUITS:
            fruits.append(item)
        elif item in TECH:
            tech.append(item)
        else:
            rest.append(item)
    write_things(cars, 'Cars')
    write_things(fruits, 'Fruits')
    write_things(tech, 'Tech')
    write_things(rest, 'Misc')


def write_things(items, kind):
    print(f"{kind.upper()} ({len(items)}st)")
    items=sorted(items)
    for item in items:
        print(f" {item}")


if __name__ == '__main__':
    run()
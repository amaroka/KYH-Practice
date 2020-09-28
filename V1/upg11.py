import random


def game(number_of_questions, max_value):
    correct_answers = 0

    for i in range(number_of_questions):
        a = random.randint(1, max_value)
        b = random.randint(1, max_value)
        while True:
            answer = input(f"{a} + {b}")
            try:
                number = int(answer)
                break
            except ValueError:
                print("Fel!! Skriv nummer.")
        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a + b}")
            print("---")
    print(f"Du fick {correct_answers} av {number_of_questions}.")


if __name__ == '__main__':
    while True:
        try:
            number = int(input("Hur många frågor: "))
            max_value = int(input("Största tal: "))
            break
        except ValueError:
            print("Bara nummer ingen skinka")
    game(number, max_value)

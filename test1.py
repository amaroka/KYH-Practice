import json
import requests
import html


class Quiz:

    def __init__(self):
        self.quiz = {}
        self.counter = 0
        self.score = 0

    def start_new(self):
        r = requests.get("https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda")
        data = json.loads(r.text)
        self.quiz = data['questions']
        self.score = 0


    def get_next(self):
        return html.unescape(self.quiz[self.counter]['prompt'])

    def display_options(self):
        print(html.unescape(self.quiz[self.counter]['rightAnswer']))
        for ic in self.quiz[self.counter]['wrongAnswers']:
            print(html.unescape(ic))
        answer = input("Ditt svar: ")
        self.check_answer(answer)

    def check_answer(self, answer):
        answer = int(answer)
        if answer == 1:
            self.score += 1
        self.counter = self.counter + 1

    def get_score(self):
        return self.score


q = Quiz()
q.start_new()
#print(f"Detta quiz innehåller {len(length)} frågor")
for i in range(10):
    print(f"Fråga {i + 1}. {q.get_next()}")
    q.display_options()
    print("")
print("***RESULTAT***")
print(f"Du fick {q.get_score()} poäng av: 10")
import requests

ENDPOINT = 'https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda'


class QuizzWebServiceAPI(object):

    def __init__(self):
        self.url = ENDPOINT

    def get_all_questions(self):
        r = requests.get(self.url)
        ls = r.json()['questions']
        return ls

    def add_question(self, prompt, answer, alternatives):
        data = {
            'prompt': prompt,
            'rightAnswer': answer,
            'wrongAnswers': alternatives
        }
        # Uppgift 35.2: fyll i ???
        r = requests.post(url=self.url, json=data)
        return True if r.status_code == 200 else False

def main():
    service = QuizzWebServiceAPI()
    while True:
        print(f"Det finns {len(service.get_all_questions())} frågor i quizz-db.\n"
                            f"1. Lägg till en fråga: \n"
                            f"2. Avsluta programmet:")
        user_choice = input("Ditt val: ")
        if user_choice == '1':
            prompt = input("Skriv en fråga: ")
            answer = input(" Vad är rätt svar?: ")
            alternatives = input("Ange två felaktiga svar med komma emellan: ").split(",")
            print(service.add_question(prompt, answer, alternatives))
            print("Tack för ditt bidrag!")
        if user_choice == '2':
            print("Programmet avslutas")
            quit()


if __name__ == '__main__':
    main()
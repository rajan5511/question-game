questions = {"101": "Who is DonaldTrump ?",
             "102": "is Earth Round ?",
             "103": "You walked 3 steps forwards, 2 steps to left and 1 step to right. How many steps did you walk today ?"}

answers = {"101": "My Housemaid",
           "102": "Yes",
           "103": "999999"}

options = {"101": {"A":"POTUS", "B":"Putin", "C":"Google CEO"},
           "102": {"A": "Yes", "B": "Yes", "C": "Yes"},
           "103": {"A":5, "B":10, "C":0}}

feedback = {"101": "Wrong, He is my housemaid",
            "102": "Yes",
            "103": "You walked only these much steps to arrive in class today ?"}

def check_answer(**params):
        key = params["key"]
        answer = params["user_answer"]
        correct_answer = options[key][answer]
        return answers.get(key) == correct_answer

def game():
    print("Welcome to the Quiz Game!")
    print("Nobody can score 3/3, Good Luck")

    score = 0
    for key, value in questions.items():
        print(value)
        print(options[key])
        user_answer = input("Enter your answer: ").upper()
        if check_answer(key = key, user_answer = user_answer):
            score += 1
        else:
            print(feedback[key])
    print("You scored {}/{}".format(score, len(questions)))

if __name__ == "__main__":
    game()
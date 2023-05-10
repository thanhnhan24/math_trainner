
import math as mth
import random
from datetime import datetime
import matplotlib.pyplot as plt

"""inlitazing the varaiable, this code run once"""

scores = []
response_times = []
wrong_answers = 0
max_wrong_answers = 3
"""============================================"""
def generate_question():
    """Tạo câu hỏi ngẫu nhiên"""
    question_type = random.choice(['arithmetic', 'equation', 'linear_equation'])
    if question_type == 'arithmetic':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2} = ?"
        answer = eval(str(num1) + operator + str(num2))
    elif question_type == 'equation':
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        question = f"{a}x + {b} = {c}"
        answer = round((c - b) / a, 2)
    else:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        question = f"{a}x^2 + {b}x + {c} = ?"
        delta = mth.pow(b,2) - 4*a*c
        while delta < 0:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            question = f"{a}x^2 + {b}x + {c} = ?"
            delta = mth.pow(b,2) - 4*a*c
        if delta == 0:
            answer = -b/2*a
        elif delta > 0:
            answer = [(-b+mth.sqrt(delta))/2*a, (-b-mth.sqrt(delta))/2*a]
    return question, answer


def play_game():
    global score, response_times, wrong_answers, max_wrong_answers, answer, final_answer, scores
    """Chơi trò chơi"""
    question, answer = generate_question()
    print(question)
    start_time = datetime.now()
    user_answer = input("Câu trả lời của bạn: ")
    if user_answer.find(';',0,len(user_answer)) == -1:
            """khong phai phuong trinh bac hai mot an"""
            final_answer = round(eval(user_answer),2)
    end_time = datetime.now()
    response_time = (end_time - start_time).total_seconds()
    response_times.append(response_time)
    



if __name__ == '__main__':
    play_game()

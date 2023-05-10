import os
person = {
    'user' : '',
    'pswd'  : '',
    'stage': 0,
    'max_stage_reached': 0,
    'total_answer': 0,
    'correct_answer': 0,
    'incorrect_answer': 0,
}

path = os.path.abspath('data') + "\\user1.data"
user_file = open(path,"+r")
user_data = user_file.write(str(person))


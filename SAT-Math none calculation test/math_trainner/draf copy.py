import os
import json
person = {
    'user' : '',
    'pswd'  : '',
    'stage': 0,
    'max_stage_reached': 0,
    'total_answer': 0,
    'correct_answer': 0,
    'incorrect_answer': 0,
}

path = os.path.abspath('data') + "\\user1.json"
user_file = open(path,"+r")
json.dump(person,user_file)


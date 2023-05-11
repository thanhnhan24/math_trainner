"""this program is to control the user data"""
"""function type is get data, write data"""
import os, json
import matplotlib.pyplot as plt
def default():
    global player,dir
    player = {
        'username' : '',
        'max_stage' : 0,
        'correct_ans' : 20,
        'incorrect_ans' : 5,
        "simple_cal" : 10,
        "first_degree_eqn" : 3,
        "quadratic_eqn" : 5,
        "trigonometric_cal" : 4,
        "area_of_basic_shapes" : 2,
        "volume_of_basic_shapes" : 1
    }
    dir = os.path.abspath("SAT-Math none calculation test")

def get(username):
    global dir
    dir += f"\\user_data\\{username}.json"
    with open(dir,'+r') as file:
        data_i = json.load(file)
        for key,value in data_i.items():
            player[key] = value
        file.close()

def write(username):
    global dir
    dir += f"\\user_data\\{username}.json"
    with open(dir,'+w') as file:
        json.dump(player,file)
        file.close()

def found(username):
    global dir
    dir += f"\\user_data\\{username}.json"
    if os.path.exists(dir):
        print("found")
    else:
        print(f"not found {username}\nplease try again")
        """return to login terminal"""

def get_status():
    global player
    statistic_categories = [
    'simple_cal',
    'first_degree_eqn',
    'quadratic_eqn',
    'trigonometric_cal',
    'area_of_basic_shapes',
    'volume_of_basic_shapes'
    ]
    accuracy_categories = [
    'correct_ans',
    'incorrect_ans'
    ]

    fig2, ax = plt.subplots(1,2, layout = 'constrained', figsize=(14, 6))
    values = [player[category] for category in statistic_categories]
    total = sum(values)
    ax[0].barh(statistic_categories, values)
    ax[0].set_xlabel(f'Quantity\nTotal answer = {total}')
    ax[0].set_ylabel('Categories')
    ax[0].set_title('Player Statistics')
    
    labels = ['Correct', 'Incorrect']
    sizes = [player['correct_ans'], player['incorrect_ans']]
    colors = ['green', 'red']
    explode = (0.1, 0)
    ax[1].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    ax[1].axis('equal')  # Đảm bảo biểu đồ tròn có hình dạng tự nhiên
    ax[1].set_title('Player Answers')  
    plt.show()






if __name__ == '__main__':
    os.system('cls')
    default()
    get_status()
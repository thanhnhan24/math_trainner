import os
import json
import time
import test
import matplotlib.pyplot as plt
def inlitazing():
    """inlitazing and login to specific user data"""
    """create local user data"""
    global player, stage,user_data
    player = {
        'user' : '',
        'pswd'  : '',
        'stage': 0,
        'max_stage_reached': 0,
        'total_answer': 0,
        'correct_answer': 0,
        'incorrect_answer': 0,
    }

    """user login panel"""
    os.system('cls')
    print("LOGIN TO USER DATA\n")
    user =  input('user :')
    password = input('password: ')

    """checking if user exist then login else create a new one"""
    if os.path.exists(f"data/{user}.json"):
        path = os.path.abspath('data') + f"\\{user}.json"
        with open(path,"+r") as file:
            user_data = json.load(file)
            
            """checking password then write data to player_data"""
            if user_data['pswd'] == password:
                print("login successful")
                for key, value in user_data.items():
                    player[key] = value
                print("\n")
                print("This is your profile:")
                print(f"user-name: {player['user']}")
                print(f"currnent-stage: {player['stage']}")
                print("Select your stage to train")
                print(f"You can select the stage from 1 to {player['max_stage_reached']}")
                stage = input("Stage select = ")
                if int(stage) <= player['max_stage_reached']:
                    print(f"Stage {int(stage)} selected || to complete the stage you'd done {int(stage)*5} equation without making over 3 mistakes")
                    time.sleep(5)
                    return game_start(int(stage))
                else:
                    print("Stage unavailable")
            else:
                print("incorrect password") 
    else:
        print("not_found")
    

def game_start(t):
    global current_stage
    for current_stage in range (0,t*5,1):
        test.play_game()
        if test.final_answer == test.answer:
            score = 1
            test.scores.append(score)
            print("Chính xác!")
            print(f"Điểm của bạn: {sum(test.scores)}")
            print()
        else:
            test.wrong_answers += 1
            if test.wrong_answers > test.max_wrong_answers:
                        print("Bạn đã trả lời sai quá 3 lần!")
                        print(f"Điểm của bạn: {sum(test.scores)}")
                        game_end('lose')
                        return None
                        
                        
            else:
                        print(f"Sai rồi! Đáp án đúng là {test.answer}. Hãy thử lại.")
                        print("\n")
    game_end('win')
    
def game_end(status):
    if(status == 'lose'):
        user_data["total_answer"] = current_stage
        user_data["correct_answer"] = sum(test.scores)
        user_data["incorrect_answer"] = test.max_wrong_answers
    elif (status == 'win'):
        plt.plot(test.response_times)
        plt.ylabel('Thời gian trả lời (giây)')
        plt.xlabel('Câu hỏi')
        plt.show()
        plt.waitforbuttonpress()
if __name__ == '__main__':
    inlitazing()
import random

def generate_sat_math_problem():
    problem_type = random.choice(['multiple_choice', 'grid_in'])
    
    if problem_type == 'multiple_choice':
        problem = generate_multiple_choice_problem()
    else:
        problem = generate_grid_in_problem()
    
    return problem

def generate_multiple_choice_problem():
    num_choices = 4
    choices = generate_random_choices(num_choices)
    correct_answer = random.choice(choices)
    problem = {
        'type': 'multiple_choice',
        'choices': choices,
        'correct_answer': correct_answer
    }
    return problem

def generate_grid_in_problem():
    correct_answer = random.randint(1, 100)
    problem = {
        'type': 'grid_in',
        'correct_answer': correct_answer
    }
    return problem

def generate_random_choices(num_choices):
    choices = []
    for _ in range(num_choices):
        choice = random.randint(1, 100)
        choices.append(choice)
    return choices

def main():
    num_problems = 5
    
    for i in range(1, num_problems + 1):
        problem = generate_sat_math_problem()
        print(f"Problem {i}:")
        if problem['type'] == 'multiple_choice':
            print("Multiple Choice")
            for j, choice in enumerate(problem['choices']):
                print(f"({chr(ord('A') + j)}) {choice}")
            print(f"Correct Answer: {chr(ord('A') + problem['choices'].index(problem['correct_answer']))}")
        else:
            print("Grid-In")
            print(f"Correct Answer: {problem['correct_answer']}")
        print()

if __name__ == '__main__':
    main()

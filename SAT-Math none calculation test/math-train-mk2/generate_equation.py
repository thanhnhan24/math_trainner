"""This program's purpose is to generate equation randomly
   All data will be save in local user data then push into json file
   By Farley == No Copyright
"""
import os, random,math

def generate_eqn():
    """this function will generate random equation
       first, we'll create some varaiable to support to the analyst
       random_choice    simple_cal  first_degree_eqn    quaratic_eqn
       trigonometric_cal    area_of_basic_shapes    volume_of_basic_shapes
    """
    global ran_choice
    ran_choice = random.choice(["simple_cal","first_degree_eqn","quaratic_eqn","trigonometric_cal","area_of_basic_shapes","volume_of_basic_shapes"])
    if ran_choice == "simple_cal":
        """case simple equation question"""
        a = random.randint(-100,100)
        b = random.randint(-100,100)
        operation = random.choice(['+','-','*'])
        question = f"{a} {operation} {b} = ?"
        ans = eval(str(a)+operation+str(b))
        return(ran_choice,question,ans)
    
    elif  ran_choice == "first_degree_eqn":
        """case first degree equation"""
        a = random.randint(-10,10)
        b = random.randint(-10,10)
        c = random.randint(-10,10)
        question = f"{a}*x {b} = {c} "
        ans = round((c-b/a),2)
        return(ran_choice,question,ans)
    
    elif ran_choice == "quaratic_eqn":
        """case quaratic equation"""
        delta = -1 #activate the while loop
        while delta < 0:
            a = random.randint(-10,10)
            b = random.randint(-10,10)
            c = random.randint(-10,10)
            delta = b*b - 4*a*c
        question = f"{a}*x^2 {b}*x + {c} = 0"
        if delta == 0:
            """case delta equal zero then the equation have only one answer"""
            ans = -b/2*a
            return(ran_choice,question,ans)
        elif delta > 0:
            """case delta greater than zero then the equation have two answer"""
            ans = [((-b + math.sqrt(delta)) / 2*a), ((-b + math.sqrt(delta)) / 2*a)]
            return(ran_choice,question,ans)

    
    
        


if __name__ == '__main__':
    os.system('cls')
    generate_eqn()

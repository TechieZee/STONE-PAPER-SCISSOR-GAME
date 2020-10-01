import random
# Taking input from the user
user_input = input("Enter any of the choices- s(Stone O) p(Paper ===) c(Scissor >8)")
if user_input.lower() == 's':
    print("O  vs",end='  ')
elif user_input.lower() == 'p':
    print("=== vs",end='  ')
elif user_input.lower() == 'c':
    print(">8 vs",end='  ')
else:
    print("Option selected is not correct!!")

# Taking input from the computer using random function
comp_selection = random.randint(1,3)
if comp_selection == 1:
    comp='s'
    print("O")
elif comp_selection == 2:
    comp='p'
    print("===")
else:
    comp='c'
    print(">8")

# Winning Logic
if user_input.lower() == comp.lower():
    print("Game is a Draw!")
elif user_input.lower() == 's' and comp.lower() =='p':
    print("Computer Wins!\nPlayer Lost!")
elif user_input.lower() == 's' and comp.lower() =='c':
    print("Player Wins!\nComputer Lost!")
elif user_input.lower() == 'p' and comp.lower() =='c':
    print("Computer Wins!\nPlayer Lost!")
elif user_input.lower() == 'p' and comp.lower() =='s':
    print("Player Wins!\nComputer Lost!")
elif user_input.lower() == 'c' and comp.lower() =='s':
    print("Computer Wins!\nPlayer Lost!")
elif user_input.lower() == 'c' and comp.lower() =='p':
    print("Player Wins!\nComputer Lost!")



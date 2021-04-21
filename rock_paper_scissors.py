#ROCK Paper Scissor Game 
# Created By Sivaprasad.G  
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
u_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
c_choice = random.randint(0, 2) 

game = [rock, paper, scissors]
choice =[u_choice, c_choice] 

if choice[0] <= 2:
    if choice[0] == 0 and choice[1] == 2:
        print(f"{game[0]}\nComputer Choice\n{game[2]}")
        print("You win")
    elif choice[0] == 2 and choice[1] == 1:
            print(f"{game[2]}\nComputer Choice\n{game[1]}")
            print("You win")
    elif choice[0] == 1 and choice[1] == 0:
            print(f"{game[1]}\nComputer Choice\n{game[0]}")
            print("You win")
    else:
        print(f"{game[choice[0]]}\nComputer Choice\n{game[choice[1]]}")
        print("You lose ") 
else:
    print("wrong number! please try again.")












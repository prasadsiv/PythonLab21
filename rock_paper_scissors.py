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
game = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_choice = random.randint(0, 2) 
choice =[user_choice, computer_choice] 

if choice[0] > 2  or choice[0] < 0:
    print("\nYou typed an invalid number, You lose!\n") 
elif choice[0] == 0 and choice[1] == 2:
    print(f"{game[0]}\nComputer Chose\n{game[2]}\nYou win\n")
elif choice[0] == 2 and choice[1] == 1:
    print(f"{game[2]}\nComputer Chose\n{game[1]}\nYou win\n")
elif choice[0] == 1 and choice[1] == 0:
    print(f"{game[1]}\nComputer Chose\n{game[0]}\nYou win\n")
elif choice[0] == choice[1]:
    print(f"{game[choice[0]]}\nComputer Chose\n{game[choice[1]]}\nit's a draw\n")
else:
    print(f"{game[choice[0]]}\nComputer Chose\n{game[choice[1]]}\nYou lose\n")












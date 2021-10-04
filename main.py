# ROCK PAPER SCISSOR - GAME

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

game_images=[rock,paper,scissors]

user_choice=int(input("What do you want to choose? 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice>=3 or user_choice<0:
  print("You have invalid number typed,You lose")
else:
  print(game_images[user_choice])

computer_choice=random.randint(0,2)
print("computer choice")
print(game_images[user_choice])

if user_choice ==0 and computer_choice ==2:
  print("User Wins!!")
elif computer_choice ==0 and user_choice ==2:
  print("User Wins!!")
elif computer_choice>user_choice:
  print("Computer wins!")
elif user_choice> computer_choice:
  print("User wins")
elif computer_choice==user_choice:
  print("Its a draw")
elif user_choice>=3:
  print("You typed invalid number,Please choose 0 to 2 ")
else:
  print("You typed invalid number")
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

import random

pick = [rock, paper, scissors]
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper 2 for Scissors \n" ))
if user_choice > 2  or user_choice < 0:
 print("YOU TYPED AN INVALID NUMBER")
else: 
  print(pick[user_choice])
    
  computer_choice = random.randint(0, 2)
  print("computer chose:")
  print(pick[computer_choice]) 
  
  if user_choice == 0 and computer_choice == 2:
    print("YOU WIN")
  elif user_choice == 1 and computer_choice == 2:
    print("YOU WIN")
  elif user_choice == 2 and computer_choice == 1:
    print("YOU WIN")
  elif user_choice == computer_choice:
    print("YOU DRAW")
  else:
    print("YOU LOOSE")
    
  
  

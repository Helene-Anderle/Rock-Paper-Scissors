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
print("Are you ready to play a game?")
person_choice = input("Choose Rock, Paper, or Scissors:\n ")
if person_choice == "rock":
    print(rock)
elif person_choice =="paper":
    print(paper)
elif person_choice =="scissors":
    print(scissors)
else:
    print("That was not a valid input")

import random
computer_list =[rock, paper, scissors]
computer_choice = random.choice(computer_list)

print(f"The Computer chooses: {computer_choice}")

if person_choice == "rock" and computer_choice == rock or person_choice == "paper" and computer_choice == paper or person_choice == "scissors" and computer_choice == scissors:
    print("You choose the same symbol! No one wins or loses")

elif person_choice == "rock" and computer_choice == scissors or person_choice == "paper" and computer_choice == rock or person_choice == "scissors" and computer_choice == paper:
    print("You won! Congratulations!")

else:
    print("You lost. Try again.")             
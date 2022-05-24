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

#Write your code below this line 👇

import random

userInput = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

signalList = [rock, paper, scissors]

userIndex = int(userInput)
computerIndex = random.randint(0, 2)

userChoice = signalList[userIndex]
computerChoice = signalList[computerIndex]

print(userChoice)
print(computerChoice)

if userIndex == computerIndex:
  print("Draw, try again!")
elif userIndex == 0 and computerIndex == 1:
  print("Paper beats rock, you lose.")
elif userIndex == 0 and computerIndex == 2:
  print("Rock beats scissors, you win!")
elif userIndex == 1 and computerIndex == 0:
  print("Paper beats rock, you win!")
elif userIndex == 1 and computerIndex == 2:
  print("Scissors beats paper, you lose.")
elif userIndex == 2 and computerIndex == 0:
  print("Rock beats scissors, you lose.")
elif userIndex == 2 and computerIndex == 1:
  print("Scissors beats paper, you win!")
else:
  print("Please enter valid input.")
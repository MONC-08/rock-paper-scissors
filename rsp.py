import sys
import random

print("")
print("Enter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors.")
playerChoice = input("Enter 1, 2 or 3\n")

player = int(playerChoice)
if(player < 1 or player >3):
    sys.exit("Enter a valid number!")

computerChoice = random.choice("123")
computer = int(computerChoice)

print("")
print("You chose:", player)
print("Python Chose:", computer)
print("")

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player == computer:
    print("It\'s a tie!")
else:
    print("Python wins!")
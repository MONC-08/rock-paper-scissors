import sys

print("Enter...\n1 for Rock,\n2 for Paper, or\n3 for Scissors.")
playerChoice = input("Enter 1, 2 or 3\n")
print(playerChoice)

player = int(playerChoice)

if(player < 1 or player >3):
    sys.exit("Enter a valid number!")
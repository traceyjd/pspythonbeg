import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

player1 = input("Enter player 1's nme: ")
player2 = input("Enter player 2's nme: ")

roll1 = roll_dice()
roll2 = roll_dice()

print(player1, "rolled", roll1)
print(player2, "rolled", roll2)


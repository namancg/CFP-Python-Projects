import math
import random


class SnakeAndLadder:
    position = 0
    dice = math.floor(random.random() * 100) % 6 + 1
    option = math.floor(random.random() * 100) % 3
    if option == 0:
        print("NO PLAY")
    elif option == 1:
        print("LADDER")
        position = position + dice
    else:
        print("SNAKE")
        position = position - dice
    print("DICE ROLLED: " + str(dice))
    print("CURRENT POSITION: " + str(position))

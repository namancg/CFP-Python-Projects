import math
import random


class SnakeAndLadder:
    position = 0
    dice = math.floor(random.random() * 100) % 6 + 1
    print("DICE ROLLED: " + str(dice))
    position = position + dice
    print("CURRENT POSITION: " + str(position))

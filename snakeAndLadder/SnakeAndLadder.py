import math
import random


class SnakeAndLadder:
    position = 0
    TOTAL_DICE_ROLLS = 0
    while position < 100:
        dice = math.floor(random.random() * 100) % 6 + 1
        TOTAL_DICE_ROLLS = TOTAL_DICE_ROLLS + 1
        option = math.floor(random.random() * 100) % 3
        if option == 0:
            print("NO PLAY")
        elif option == 1:
            print("LADDER")
            position = position + dice
            if position > 100:
                position = position - dice
        elif option == 2:
            print("SNAKE")
            position = position - dice
            if position < 0:
                position = 0
        print("DICE ROLLED: " + str(dice))
        print("CURRENT POSITION: " + str(position))
        print("TOTAL DICE ROLLS: "+str(TOTAL_DICE_ROLLS))
    print("WINNER")
    print("TOOK "+str(TOTAL_DICE_ROLLS)+" NO OF DICE ROLLS TO WIN")

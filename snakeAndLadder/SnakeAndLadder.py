import math
import random


class SnakeAndLadder:
    POSITION_PLAYER_1 = 0
    POSITION_PLAYER_2 = 0
    iteration = 0
    position = 0
    while POSITION_PLAYER_1 < 100 & POSITION_PLAYER_2 == 0:
        if iteration % 2 == 0:
            position = POSITION_PLAYER_1
            print("PLAYER 1's TURN WHO IS AT: " + str(POSITION_PLAYER_1))
        else:
            position = POSITION_PLAYER_2
            print("PLAYER 2's TURN WHO IS AT: " + str(POSITION_PLAYER_2))
        iteration = iteration + 1

        dice = math.floor(random.random() * 100) % 6 + 1
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

        if (iteration - 1) % 2 == 0:
            POSITION_PLAYER_1 = position
        else:
            POSITION_PLAYER_2 = position
        print("CURRENT POSITION OF PLAYER 1: " + str(POSITION_PLAYER_1))
        print("CURRENT POSITION OF PLAYER 2: " + str(POSITION_PLAYER_2))
        if option == 1:
            iteration = iteration - 1
    if POSITION_PLAYER_1 == 100:
        print("PLAYER 1 IS THE WINNER")
    else:
        print("PLAYER 2 IS THE WINNER")

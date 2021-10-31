import random

score_1 = random.randint(0,50)
score_2 = random.randint(0,50)

if score_1 > 50:
    print("Please check the input score for '1'.")
elif score_2 > 50:
    print("Please check the input score for '2'.")
else:
    print("Score validated. Your total is: ",score_1 + score_2)
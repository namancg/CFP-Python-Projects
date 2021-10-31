import random

isPresent = 1
emp = random.randint(0,1)
wagePerHour=20
if emp == isPresent:
    print("EMPLOYEE IS PRESET")
    workingHours = 8
else:
    print("EMPLOYEE IS ABSENT")

wage=workingHours+wagePerHour
print(wage)



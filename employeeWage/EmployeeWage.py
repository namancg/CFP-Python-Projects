import random

isPresent = 1
isPartTime=2
emp = random.randint(0, 2)
wagePerHour=20
if emp == isPresent:
    print("EMPLOYEE IS FULL TIME")
    workingHours = 8
elif emp == isPartTime:
    print("EMPLOYEE IS PART TIME")
    workingHours = 4
else:
    print("EMPLOYEE IS ABSENT")
wage=workingHours+wagePerHour
print(wage)



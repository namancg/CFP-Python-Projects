import random

isAbsent = 0
isPresent = 1
isPartTime = 2
totalWage = 0
wagePerHour = 20
noOfWorkingDays = 20
workingHour = 0
for i in range(noOfWorkingDays):
    emp = random.randint(0, 2)
    if emp == isPresent:
        print("EMPLOYEE IS FULL TIME")
        workingHours = 8
    elif emp == isPartTime:
        print("EMPLOYEE IS PART TIME")
        workingHours = 4
    else:
        print("EMPLOYEE IS ABSENT")
wage = workingHours * wagePerHour
totalWage = totalWage + wage
print(wage)

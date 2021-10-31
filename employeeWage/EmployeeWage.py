import random

isAbsent = 0
isPresent = 1
isPartTime = 2
totalWage = 0
wagePerHour = 20
noOfWorkingDays = 20
maxHoursInAMonth = 100
workingHour = 0
totalWorkingDays = 0
totalEmployeeHours = 0
while totalWorkingDays < noOfWorkingDays and totalEmployeeHours <= maxHoursInAMonth:
    emp = random.randint(0, 2)
    if emp == isPresent:
        print("EMPLOYEE IS FULL TIME")
        workingHours = 8
    elif emp == isPartTime:
        print("EMPLOYEE IS PART TIME")
        workingHours = 4
    else:
        print("EMPLOYEE IS ABSENT")
    totalEmployeeHours=totalEmployeeHours+workingHour
    totalWorkingDays=totalWorkingDays+1
wage = workingHours * wagePerHour
totalWage = totalWage + wage
print(wage)

import random


class EmployeeWage:
    """CLASS THAT CONTAINS EMPLOYEE WAGE CALCULATION"""
    isAbsent = 0
    isPresent = 1
    isPartTime = 2
    totalWage = 0
    wagePerHour = 20
    noOfWorkingDays = 20
    maxHoursInAMonth = 100
    workingHours = 0

    def __init__(self, companyName, wagePerHour, noOfWorkingDays, maxHoursInAMonth):
        """TO INITIALIZE INSTANCE VARIABLE"""
        self.companyName = companyName
        self.noOfWorkingDays = noOfWorkingDays
        self.wagePerHour = wagePerHour
        self.maxHoursInAMonth = maxHoursInAMonth

    def getEmployeeWage(self):
        """METHOD THAT CALCULATES EMPLOYEE WAGE"""
        totalWorkingDays = 0
        totalEmployeeHours = 0
        while totalWorkingDays < self.noOfWorkingDays and totalEmployeeHours <= self.maxHoursInAMonth:
            emp = random.randint(0, 2)
            if emp == self.isPresent:
                print("EMPLOYEE IS FULL TIME")
                workingHours = 8
            elif emp == self.isPartTime:
                print("EMPLOYEE IS PART TIME")
                workingHours = 4
            else:
                print("EMPLOYEE IS ABSENT")
                workingHours = 0
            totalEmployeeHours = totalEmployeeHours + workingHours
            totalWorkingDays = totalWorkingDays + 1
            wage = workingHours + self.wagePerHour
        totalWage = totalEmployeeHours + self.wagePerHour
        print("DAILY WAGE: " + str(wage))
        print(self.companyName)
        print("TOTAL WAGE: " + str(totalWage))


# totalEmployeeWage.getEmployeeWage()
# print("TOTAL WAGE: " + str(totalEmployeeWage.totalWage))
totalEmployeeWage = EmployeeWage("PERFIOS", 20, 20, 100)
totalEmployeeWage.getEmployeeWage()
totalEmployeeWage = EmployeeWage("FORMULA 1", 30, 60, 80)
totalEmployeeWage.getEmployeeWage()
totalEmployeeWage = EmployeeWage("MERCEDES", 40, 30, 90)
totalEmployeeWage.getEmployeeWage()

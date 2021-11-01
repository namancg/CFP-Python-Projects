import random


class EmployeeWage:
    isAbsent = 0
    isPresent = 1
    isPartTime = 2
    totalWage = 0
    wagePerHour = 20
    noOfWorkingDays = 20
    maxHoursInAMonth = 100
    workingHours = 0

    def getEmployeeWage(self):
        totalWorkingDays = 0
        totalEmployeeHours = 0
        while totalWorkingDays < self.noOfWorkingDays and totalEmployeeHours <= self.maxHoursInAMonth:
            emp = random.randint(0, 2)
            if emp == self.isPresent:
                workingHours = 8
            elif emp == self.isPartTime:
                print("EMPLOYEE IS PART TIME")
                workingHours = 4
            else:
                print("EMPLOYEE IS ABSENT")
                workingHours = 0
            totalEmployeeHours = totalEmployeeHours + workingHours
            totalWorkingDays = totalWorkingDays + 1
        self.totalWage = totalEmployeeHours + self.wagePerHour


totalEmployeeWage = EmployeeWage()
totalEmployeeWage.getEmployeeWage()
print("TOTAL WAGE: " + str(totalEmployeeWage.totalWage))

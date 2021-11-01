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

    def getEmployeeWage(self,companyName,wagePerHour,noOfWorkingDays,maxHoursInAMonth):
        """METHOD THAT CALCULATES EMPLOYEE WAGE"""
        totalWorkingDays = 0
        totalEmployeeHours = 0
        while totalWorkingDays < noOfWorkingDays and totalEmployeeHours <= maxHoursInAMonth:
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
        totalWage = totalEmployeeHours + wagePerHour
        print(companyName)
        print("TOTAL WAGE: "+str(totalWage))


totalEmployeeWage = EmployeeWage()
#totalEmployeeWage.getEmployeeWage()
#print("TOTAL WAGE: " + str(totalEmployeeWage.totalWage))
totalEmployeeWage.getEmployeeWage("PERFIOS",20,20,100)
totalEmployeeWage.getEmployeeWage("FORMULA 1",30,60,80)
totalEmployeeWage.getEmployeeWage("MERCEDES",40,30,90)


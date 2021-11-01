import random


class EmployeeWage:
    """CLASS THAT CONTAINS EMPLOYEE WAGE CALCULATION"""
    IS_ABSENT = 0
    IS_PRESENT = 1
    IS_PART_TIME = 2
    TOTAL_WAGE = 0
    WAGE_PER_HOUR = 20
    NO_OF_WORKING_DAYS = 20
    MAX_HRS_IN_A_MONTH = 100
    workingHours = 0

    def __init__(self, companyName, WAGE_PER_HOUR, NO_OF_WORKING_DAYS, MAX_HRS_IN_A_MONTH):
        self.companyName = companyName
        self.NO_OF_WORKING_DAYS = NO_OF_WORKING_DAYS
        self.WAGE_PER_HOUR = WAGE_PER_HOUR
        self.MAX_HRS_IN_A_MONTH = MAX_HRS_IN_A_MONTH

    def getEmployeeWage(self):
        """METHOD THAT CALCULATES EMPLOYEE WAGE"""
        TOTAL_WORKING_DAYS = 0
        TOTAL_EMPLOYEE_HOURS = 0
        while TOTAL_WORKING_DAYS < self.NO_OF_WORKING_DAYS and TOTAL_EMPLOYEE_HOURS <= self.MAX_HRS_IN_A_MONTH:
            emp = random.randint(0, 2)
            if emp == self.IS_PRESENT:
                print("EMPLOYEE IS FULL TIME")
                workingHours = 8
            elif emp == self.IS_PART_TIME:
                print("EMPLOYEE IS PART TIME")
                workingHours = 4
            else:
                print("EMPLOYEE IS ABSENT")
                workingHours = 0
            TOTAL_EMPLOYEE_HOURS = TOTAL_EMPLOYEE_HOURS + workingHours
            TOTAL_WORKING_DAYS = TOTAL_WORKING_DAYS + 1
            wage = workingHours + self.WAGE_PER_HOUR
        TOTAL_WAGE = TOTAL_EMPLOYEE_HOURS + self.WAGE_PER_HOUR
        print("DAILY WAGE: " + str(wage))
        print(self.companyName)
        print("TOTAL WAGE: " + str(TOTAL_WAGE))


# TOTAL_EMPLOYEE_WAGE.getEmployeeWage()
# print("TOTAL WAGE: " + str(TOTAL_EMPLOYEE_WAGE.TOTAL_WAGE))
TOTAL_EMPLOYEE_WAGE = EmployeeWage("PERFIOS", 20, 20, 100)
TOTAL_EMPLOYEE_WAGE.getEmployeeWage()
TOTAL_EMPLOYEE_WAGE = EmployeeWage("FORMULA 1", 30, 60, 80)
TOTAL_EMPLOYEE_WAGE.getEmployeeWage()
TOTAL_EMPLOYEE_WAGE = EmployeeWage("MERCEDES", 40, 30, 90)
TOTAL_EMPLOYEE_WAGE.getEmployeeWage()

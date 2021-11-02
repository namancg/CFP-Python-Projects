import random
from company_employee_wage import CompanyEmployeeWage


class EmployeeWage:
    """CLASS THAT CONTAINS EMPLOYEE WAGE CALCULATION"""
    IS_ABSENT = 0
    IS_PRESENT = 1
    IS_PART_TIME = 2
    company_employee_wage_list = []

    def add_employee_wage(self, company_name, WAGE_PER_HOUR, NO_OF_WORKING_DAYS, MAX_HRS_IN_A_MONTH):
        self.company_employee_wage_list.append(
            CompanyEmployeeWage(company_name, WAGE_PER_HOUR, NO_OF_WORKING_DAYS, MAX_HRS_IN_A_MONTH))

    def calculate_company_employee_wage(self):
        for i in range(len(self.company_employee_wage_list)):
            self.company_employee_wage_list[i].set_total_employee_wage(
                self.getEmployeeWage(self.company_employee_wage_list[i]))
        print(self.company_employee_wage_list[i])

    def getEmployeeWage(self, Employee):
        """METHOD THAT CALCULATES EMPLOYEE WAGE"""
        TOTAL_WORKING_DAYS = 0
        TOTAL_EMPLOYEE_HOURS = 0
        while TOTAL_EMPLOYEE_HOURS < Employee.MAX_HRS_IN_A_MONTH and TOTAL_WORKING_DAYS < Employee.NO_OF_WORKING_DAYS:
            emp = random.randint(0, 2)
        if emp == self.IS_PRESENT:
            print("EMPLOYEE IS FULL TIME")
            working_hours = 8
        elif emp == self.IS_PART_TIME:
            print("EMPLOYEE IS PART TIME")
            working_hours = 4
        else:
            print("EMPLOYEE IS ABSENT")
            working_hours = 0
        TOTAL_EMPLOYEE_HOURS = TOTAL_EMPLOYEE_HOURS + working_hours
        TOTAL_WORKING_DAYS = TOTAL_WORKING_DAYS + 1
        print(Employee.company_name)
        print("TOTAL WAGE: {0}".format(str(TOTAL_EMPLOYEE_HOURS * Employee.WAGE_PER_HOUR)))
        return TOTAL_EMPLOYEE_HOURS * Employee.WAGE_PER_HOUR


employee = EmployeeWage()
employee.add_employee_wage("PERFIOS", 20, 20, 10)
employee.add_employee_wage("FORMULA 1", 30, 60, 20)
employee.add_employee_wage("MERCEDES", 40, 30, 20)
employee.calculate_company_employee_wage()

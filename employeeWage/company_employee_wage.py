class CompanyEmployeeWage:
    TOTAL_WAGE = 0

    def __init__(self, company_name, WAGE_PER_HOUR, NO_OF_WORKING_DAYS, MAX_HRS_IN_A_MONTH):
        self.company_name = company_name
        self.NO_OF_WORKING_DAYS = NO_OF_WORKING_DAYS
        self.WAGE_PER_HOUR = WAGE_PER_HOUR
        self.MAX_HRS_IN_A_MONTH = MAX_HRS_IN_A_MONTH

    def set_total_employee_wage(self, TOTAL_WAGE):
        self.TOTAL_WAGE = TOTAL_WAGE

    def __str__(self):
        return "TOTAL EMPLOYEE WAGE FOR COMPANY: "+str(self.company_name)+" IS "+str(self.TOTAL_WAGE)

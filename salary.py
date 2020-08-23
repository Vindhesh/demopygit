class GetSalary:
    def __init__(self, name, net_salary):
        self.name = name
        self.net_salary = net_salary
    
    # def enterDetails(self):
    #     name = input("Enter name: ")
    #     salary = input("Enter Salary amount: ")

    def get_details(self):
        print("The name of Employee is: ", self.name)
        print("The Salary of Employee is: ", self.net_salary)

employee = GetSalary("Rohan", 1200)
# employee.enterDetails()
employee.get_details()
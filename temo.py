# class Employee:
#     name = 'Ben'
#     designation = 'Sales_Executive'
#     salesMadeThisWeek = 6

#     def hasAchievedTarget(self):
#         if salesMadeThisWeek >= 5:
#             print('Target has been achieved')
#         else: print('Target has not been achieved')

# employeeOne = Employee()
# print(employeeOne.name)
# employeeOne.salesMadeThisWeek = 7
# print(employeeOne.hasAchievedTarget)

class Employee:
        NumberOfWorkingHours = 40

employeeOne = Employee()
employeeTwo = Employee()
employeeOne.NumberOfWorkingHours = 45
print(employeeOne.NumberOfWorkingHours)

employeeOne.name = 'John'
employeeTwo.name = 'Mary'

print(employeeTwo.name)

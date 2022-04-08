from module.employee import Employee

my_employee = Employee()

# Showing the resuts
print(f"The Salary of an employee is:{my_employee.display_record()}")
print(my_employee.give_raise())
print(my_employee.give_raise(100))


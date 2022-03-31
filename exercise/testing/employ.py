from module.employee import Employee

first = "First Name: "
last = "Last Name: "
salary = "Salary: "

my_employee = Employee(first, last, salary)
my_employee.get_data()

print("Enter 'q' to quit any time you want.")
while True:
    first = input("\nFirst Name: ")
    if first == 'q' or first == 'q'.upper():
        break
    last = input("\nLast Name: ")
    if last == 'q' or last == 'q'.upper():
        break
    salary = input("\nSalary: ")
    if salary == 'q' or salary == 'q'.upper():
        break
    my_employee.stored_data(first,last, salary)

# Display Data
print("The following are the records of an employee's: ")
my_employee.display_record()
my_employee.give_raise(500)
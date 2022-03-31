import unittest

from module.employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Testing the Employee Class."""

    def setUp(self) :
        first = "First Name: "
        last = "Last Name: "
        salary = "Salary: "
        self.my_employee = Employee(first, last, salary)
        self.store = ['Aayush', 'Nepal', 1000]
    
    def test_give_default_raise(self):
        """Testing a salary raise for an employee."""
        self.my_employee.stored_data(self.store)
        self.assertIn(self.store[0], self.my_employee)
    
    def test_give_custom_raise(self):
        self.my_employee.store_data(self.store)


if __name__ == '__main__':
    unittest.main()
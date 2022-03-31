import unittest

from module.employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Testing the Employee Class."""

    def setUp(self) :
        self.my_employee = Employee(first='Aayush', last='Nepal', salary='1000')
        self.store_data = ('Aayush', 'Nepal', '1000')
    
    def test_give_default_raise(self):
        """Testing a salary raise for an employee."""
        for store in self.store_data:
            self.my_employee.stored_data(store)
        for store in self.store_data:
            self.assertIn(store, self.my_employee.store_data)


    def test_give_custom_raise(self):
        "Test all the employee salaries and there raise of the salaries"
        for store in self.store_data:
            self.my_employee.stored_data(store)
        for store in self.store_data:
            self.assertIn(store, self.my_employee.store_data)

if __name__ == '__main__':
    unittest.main()
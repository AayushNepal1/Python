import unittest

from module.employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Testing the Employee Class."""

    def setUp(self) :
        self.my_employee = Employee()
    
    def test_give_default_raise(self):
        """Testing a salary raise for an employee."""
        test_case_I = self.my_employee.give_raise()
        self.assertNotEqual(test_case_I, self.my_employee.give_raise())


    def test_give_custom_raise(self):
        "Test all the employee salaries and there raise of the salaries"
        salary_test = self.my_employee.give_raise(1000)
        self.assertNotEqual(salary_test, self.my_employee.give_raise(1000))


if __name__ == '__main__':
    unittest.main()
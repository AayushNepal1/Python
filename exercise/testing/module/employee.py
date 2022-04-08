class Employee:
    """Creating an Employee Class."""
    
    
    def __init__(self):
        "Entering the first name last name and the salary of an employee."
        self.salary = int()
    
    def give_raise(self, raise_amount=5000):
        """Incrementing the salary of an employee."""
        self.salary = self.salary + raise_amount
        return f"The incremented anual salary of an employee is: {int(self.salary)}"
    
    def display_record(self):
        """Displaying the information of an employee."""
        return self.salary
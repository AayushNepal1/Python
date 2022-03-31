class Employee:
    """Creating an Employee Class."""
    
    
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.store_data = []
        
    def get_data(self):
        """Displaying The Questions"""
        print("Enter your First Name, Last Name and Anual Salary: ")

    def give_raise(self, increase=5000):
        """Increment the salary of the Employee."""
        amount = self.salary
        if amount.isdigit():
            self.salary = self.salary + increase
        
    def stored_data(self, *data):
        """Store the employee data."""
        self.store_data.append(data)

 
    def display_record(self):
        for data in self.store_data:
            for emp in data:
                print(f"- {emp}")
            print("------------------")
        print()
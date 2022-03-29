class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = 0
        # user_profile = {'first_name': self.first_name, 'last_name': self.last_name}
        # for key, value in user_profile.items():
        #     print(f"{key}: {value}")

    def describe_user(self):
        print(f"My name is {self.first_name.title()} {self.last_name.title()}.")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!") 

    def increment_login_attempts(self):
        self.login_attempt += 1
        print(self.login_attempt)
    
    def reset_login_attempts(self):
        self.login_attempt = 0
        print(self.login_attempt)

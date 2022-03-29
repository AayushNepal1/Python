from .user import Users
from .priviledge import Previleges

class Admin(Users):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        
        self.previledge = Previleges()
    

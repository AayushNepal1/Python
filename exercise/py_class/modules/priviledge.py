class Previleges:
    def __init__(self, privilege=""):
        
        privilege = [
            "can add post",
            "can ban users",
            "can delete users",
        ]

        self.privilege = privilege

    def show_privilege(self):
        for privileges in self.privilege:
            print(f"Admin: {privileges}")


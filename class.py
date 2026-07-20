class Name:
    def __init__(self, firstname, lastname='prospa'):
        self.firstname = firstname
        
    
    def get_name(self):
        return f"{self.firstname}"
    
    
# =====object====

user = Name('Joshua')
print(user.firstname)

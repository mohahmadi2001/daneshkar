import uuid

class User:
    id_counter = 0
    users = []
    
    def __init__(self, username, password, phone_number = None) :
        if username in User.users:
            raise ValueError("This username already exists.")
        self.username = username
        self.users.append(username)
    
    

u1 = User("alii")
u2 = User("ali")
print(u1)
print(u2)
    
    
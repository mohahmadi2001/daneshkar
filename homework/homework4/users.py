import uuid

class User:
    id_counter = 0
    users = []
    
    def __init__(self, username, password, phone_number = None) :
        if username in self.users:
            raise ValueError("This username already exists.")
        self.username = username
        self.users.append(username)
        self.__password = None
        self.password = password
        self.phone_number = phone_number
        User.id_counter += 1
        self.id = User.id_counter
       
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long.")
        self.__password = password
        
    def __str__(self) -> str:
        return f"{self.id},{self.username} : {self.__password}"

u1 = User("mohammad","1234")
u2 = User("ali","4321")
print(u1)
print(u2)
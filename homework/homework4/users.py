import uuid
"""
    In this module, a user class is created that stores user information
    including username, password and phone number
"""
class User:
    # id_counter = 0
    users = {}
    
    def __init__(self, username: str, password: str, phone_number : int = None) :
        if username in self.users:
            raise ValueError("This username already exists.")
        self.username = username
        User.users[self.username] = self
        self.__password = None
        self.password = password
        self.phone_number = phone_number
        # User.id_counter += 1
        # self.id = User.id_counter
        self.id = uuid.uuid4().int
       
        
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, password : str):
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long.")
        self.__password = password
        
    @staticmethod
    def valid_password(old_password: int,new_password: int,confirm_password: int) -> int:
        """
        In this function, the user's password is validated

        Args:
            old_password (int): old password
            new_password (int): new password
            confirm_password (int): confirm password

        Raises:
            ValueError: if old password is incorrect.
            ValueError: if new passwords do not match.

        Returns:
            int: new password
        """
        if old_password != User.current_user.password:
            raise ValueError("Old password is incorrect.")
        if new_password != confirm_password:
            raise ValueError("New passwords do not match.")
        User.current_user.password = new_password
        print("Password successfully changed.")

        
    
    def __str__(self) -> str:
        return f"ID:{self.id}, Username: {self.username}, Phone Number: {self.phone_number}"


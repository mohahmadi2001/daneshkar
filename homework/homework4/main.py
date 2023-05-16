"""
In this module, the previously created user class is used
"""
from users import User
import getpass

def register_user():
    """
    In this function, user registering user is checked
    """
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password (at least 4 characters): ")
    phone_number = input("Enter a phone number (optional): ")
    User(username,password,phone_number)

def login_user():
    """
    In this function, user login is checked
    """
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    if username not in User.users:
        print("This username does not exist.")
        return
    User.current_user = User.users[username]
    
    if User.users[username].password != password:
        print("Incorrect password.")
        return
    print("Login successful.")
    

def edit_user():
    """
    In this function, edit user is checked
    """
    print("1. Edit username")
    print("2. Edit phone number")
    choice = int(input("Enter choice: "))
    if choice == 1:
        new_username = input("Enter new username: ")
        if new_username in User.users:
            print("Username already exists.")
        else:
            User.users.pop(User.current_user.username)
            User.current_user.username = new_username
            User.users[new_username] = User.current_user
            print("Username successfully changed.")
    elif choice == 2:
        new_phone_number = getpass.getpass("Enter your password: ")
        User.current_user.phone_number = new_phone_number
        print("Phone number successfully changed.")
    else:
        print("Invalid choice.")

def change_password():
    """
    In this function, user can change password
    """
    old_password = getpass.getpass("Enter old password: ")
    new_password = getpass.getpass("Enter new password: ")
    confirm_password = getpass.getpass("Confirm new password: ")
    try:
        User.valid_password(old_password, new_password, confirm_password)
    except ValueError as e:
        print(e)

    
    

while True:
    print("1. Register user")
    print("2. Login user")
    print("0. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        register_user()
    elif choice == 2:
        login_user()
        if User.current_user:
            while True:
                print("1. View user information")
                print("2. Edit user information")
                print("3. Change password")
                print("4. Logout")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    print(User.current_user)
                elif choice == 2:
                    edit_user()
                elif choice == 3:
                    change_password()
                elif choice == 4:
                     break
                else:
                    print("Invalid choice.")
                    
    elif choice == 0:
        break
    else:
        print("Invalid choice.")

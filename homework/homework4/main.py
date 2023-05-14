from users import User

users = {}

def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password (at least 4 characters): ")
    phone_number = input("Enter a phone number (optional): ")

    new_user = User(username,password,phone_number)
    users[new_user.id] = new_user
    
    
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username not in users:
        print("This username does not exist.")
        return
    user = users[username]
    
    if user.password != password:
        print("Incorrect password.")
        return
    while True:
        choice = input("Enter 1 to view your profile, 2 to edit your profile, 3 to change your password, or 4 to log out: ")
        
        if choice == "1":
            print(user)
        elif choice == "2":
            new_username = input("Enter a new username (or press enter to keep the current one): ")
            if new_username:
                users.pop(username)
                user.username = new_username
                users[username] = user
            new_phone_number = input("Enter a new phone number (or press enter to keep the current one): ")
            user.phone_number = new_phone_number
        elif choice == "3":
            old_password = input("Enter your old password: ")
            new_password = input("Enter a new password (at least 4 characters): ")
            confirm_password = input("Enter the new password again: ")
            
            if old_password != user.password:
                print("Incorrect password.")
                continue
            if new_password != confirm_password:
                print("Passwords do not match.")
                continue
            user.password = new_password
            print("Password changed successfully.")
            
        elif choice == "4":
            return
        else:
            print("Invalid choice.")
            
            
while True:
    choice = input("Enter 1 to register a new user, 2 to log in, or 0 to exit: ")
    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "0":
        break
    else:
        print("Invalid choice.")
               
                
    
    
    
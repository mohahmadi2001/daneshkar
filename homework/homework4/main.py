from users import User

users = {}

while True:
    
    print("Please select an option:")
    print("0 - Exit")
    print("1 - Register a new user")

    choice = input("Enter your choice: ")
    
    if choice == "0":
        print("Exiting the program...")
        break
    
    elif choice == "1":
        
        username = input("Enter a username: ")
        password = input("Enter a password (minimum 4 characters): ")
        phone_number = input("Enter a phone number (optional): ")
        
        new_user = User(username, password, phone_number)
        
        users[new_user.id] = new_user
        
        print(f"New user {username} created with id {new_user.id}")
        
    
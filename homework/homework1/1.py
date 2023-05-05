username = input("Please Enter Your Username: ")
password = input("Please Enter Your Password: ")
if username == "admin" and password == "admin":
    print("Welcome")
elif username == "admin":
    print("Wrong Data")
else:
    print("Hello",username)
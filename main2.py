# input user name and password
# if user name and password are correct, print "Welcome"
# if user name and password are not correct, print "Wrong user name or password"

username = input("Enter user name: ")
if username == "admin":
    password = input("Enter password: ")
    if password == "1234":
        print("Welcome")
    else:
        print("Wrong password")

else:
    print("Wrong user name")
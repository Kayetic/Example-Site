x = 1
password = "Tues1212"
while x < 3:
    user_password = input("Enter password: ")
    if user_password == password:
        print("Password accepted")
        break
    else:
        print("Password rejected")
        x += 1

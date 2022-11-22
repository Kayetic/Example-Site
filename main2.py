def getPword(attempt):
    if attempt == 1:
        user_password = input("Enter your password: ")
        if len(user_password) < 6 or len(user_password) > 8:
            print("Password must be at least 8 characters long.")
            return getPword(1)
    elif attempt == 2:
        if len(user_password) < 6 or len(user_password) > 8:
            print("Password must be at least 8 characters long.")
            return getPword(2)
        user_password = input("Enter the password again: ")
    return user_password


def main():
    user_password = getPword(1)
    if user_password == getPword(2):
        print("Password accepted.")
    else:
        print("Password does not match.")


main()

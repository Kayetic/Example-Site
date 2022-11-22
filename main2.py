
def multiples(table, startnum, endnum):
    for i in range(startnum, endnum + 1):
        print(table, "x", i, "=", table * i)
    print()


# main program
name = input("What is your name?\n")
print("Enter times table, start number and end number")
user_table = int(input())
user_startnum = int(input())
user_endnum = int(input())

print(f"Hi {name} ... here is your times table")
multiples(user_table, user_startnum, user_endnum)

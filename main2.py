mark = int(input("Enter your exam mark: "))
attendance = int(input("Enter your attendance percentage: "))
if attendance > 90:
    if mark > 90:
        grade = "A"
    elif mark > 80 and mark <= 90:
        grade = "B"
    elif mark > 70 and mark <= 80:
        grade = "C"
    elif mark <= 70:
        fail = True
    if fail:
        print("Failed")
    else:
        print("Grade: ", grade)
else:
    fail = True
    print("Failed")

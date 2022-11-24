names = []


def addName():
    name = input("Enter the name to be added to the list: ")
    position = int(input("Enter the position to add the name: "))
    names.insert(position, name)


def listNames():
    print("The names in the list are: ")
    for name in names:
        print(names.index(name), name)


def displayMenu():
    while True:
        choice = input("""
1 Add name
2 Display list
3 Quit
: """)
        if choice != "1" and choice != "2" and choice != "3":
            print("Invalid choice")
            continue
        else:
            return choice


choice = displayMenu()
if choice == "1":
    addName()
elif choice == "2":
    listNames()
elif choice == "3":
    print("Program Terminating")
    exit()

total = 0
old = 0

while True:
    while True:
        part_number = input("Enter part number: ")
        if len(part_number) != 4:
            print("Invalid part number. Must be 4 characters long.")
        else:
            break
    if part_number == "9999":
        break
    total += 1
    if part_number[3] == "6" or part_number[3] == "7" or part_number[3] == "8":
        old += 1

print("Total parts: ", total)
print("Old parts: ", old)

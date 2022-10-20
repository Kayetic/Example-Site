paper_bags = int(input("Enter the number of paper bags: "))
sweets = int(input("Enter the number of sweets: "))
if sweets < paper_bags: exit("You should have more sweets than paper bags")
print("Possible for uneven number") if sweets % paper_bags != 0 else print("Impossible for uneven number")

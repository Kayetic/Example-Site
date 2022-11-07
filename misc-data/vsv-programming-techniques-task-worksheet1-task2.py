import math

width_of_room = float(input("Width of room in meters? "))
length_of_room = float(input("Length of room in meters? "))
height_of_room = float(input("Height of room in meters? "))
no_paint = input("\nSurface area of room not to paint in square meters? (leave blank if none) ")
if no_paint == "":
    no_paint = 0
else:
    no_paint = float(no_paint)
coats_of_paint = input("\nHow many coats of paint to apply? (leave blank for just one) ")
if coats_of_paint == "":
    coats_of_paint = 1
else:
    coats_of_paint = float(coats_of_paint)
total = 0

# calculating surface area of room
base_and_top = 2 * (float(width_of_room) * float(length_of_room))
sides1 = 2 * (float(width_of_room) * float(height_of_room))
sides2 = 2 * (float(length_of_room) * float(height_of_room))
total = base_and_top + sides1 + sides2
total -= no_paint

print("The total surface area to paint is " + str(total) + " square meters.")

total = total * coats_of_paint
paint_cans = total / 11

# rounds up the number of cans required
paint_cans = math.ceil(paint_cans)
print("You will need " + str(paint_cans) + " cans of paint.")

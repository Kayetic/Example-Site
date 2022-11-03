import math


width_of_room = float(input("What is the width of the room in meters? "))
length_of_room = float(input("What is the length of the room in meters? "))
height_of_room = float(input("What is the height of the room in meters? "))
surface_area_to_not_paint = float(input("\nWhat is the surface area of the room that you do not want to paint in square meters? "))
coats_of_paint = float(input("\nHow many coats of paint do you want to apply? "))
total = 0

base_and_top = 2 * (float(width_of_room) * float(length_of_room))
sides1 = 2 * (float(width_of_room) * float(height_of_room))
sides2 = 2 * (float(length_of_room) * float(height_of_room))
total = base_and_top + sides1 + sides2
total -= surface_area_to_not_paint

print("The total surface area to paint is " + str(total) + " square meters.")

paint_cans = total / 11
paint_cans = math.ceil(paint_cans)
print(paint_cans)

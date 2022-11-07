last_car_mileage = int(input("Enter the mileage since last time car was filled: "))
current_car_mileage = int(input("Enter the current mileage of the car: "))
covered_mileage = current_car_mileage - last_car_mileage
total_litres = int(input("Enter the total litres taken to fill the tank: "))
gallons = total_litres / 4.546
miles_per_gallon = covered_mileage / gallons
print("The miles per gallon is: ", miles_per_gallon)
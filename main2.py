order = float(input("Enter the total value of the order: "))
next_day = input("Do you want next day delivery? (Y/N): ")
total = 0
postal_charge = 0
if next_day == "Y":
    total = order + 5
    postal_charge = 5
else:
    if order >= 15:
        total = order
        postal_charge = 0
    else:
        total = order + 3.50
        postal_charge = 3.50

print("Postal charge: £", postal_charge)
print("Total: £", total)

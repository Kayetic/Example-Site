# problem:

# 1. Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.
# sort list, check if number is >= 0, sum them

def sumPositive(list):
    list.sort()
    for number in list:
        print(number)
        if number < 0:
            removed = list.pop(number)
        else:
            continue
    return list


list = [1, 4, 12, 5, -1, -9, 0, 13, 55, 2, -123]
print(sumPositive(list))

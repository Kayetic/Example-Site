# 1, 3, 3, 9, 12
# target = 6

array = [1, 3, 3, 9, 12]
target = int(input('Enter a target number: '))
for firstNumber in array:
    if firstNumber >= target:
        continue
    else:
        for secondNumber in array:
            if firstNumber + secondNumber == target:
                print(
                    f'Done, indexes: {array.index(firstNumber)}, {array.index(secondNumber)}')
            else:
                continue

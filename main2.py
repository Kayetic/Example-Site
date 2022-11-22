letters = []
for i in range(5):
    letters.append(ord(input("Enter a letter: ")))
print("The largest letter is", chr(max(letters)))
print("The smallest letter is", chr(min(letters)))

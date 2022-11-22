total = 0
average_scores = []
for i in range(30):
    student_score = 0
    for j in range(3):
        score = int(input(f"Enter the student's score for test {j+1}: "))
        student_score += score
    average = round(student_score / 3, 2)
    print(f"The student's average score is {average}")
    average_scores.append(average)
    total += student_score
print(f"The class average is {round(total/90), 2}")
print("Individual student scores:")
for i in range(len(average_scores)):
    print(f"Student {i+1}: {average_scores[i]}")

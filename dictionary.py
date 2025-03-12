colors= {
    "tomato" : "red",
    "onion" : "pink",
    "capsicum" : "green"
}
print(colors["tomato"])
colors["tomato"] = "red cheery"
print(colors["tomato"])
x = colors.keys()
print(x)

# dictionary program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades [student] = "outstanding"

    elif score >= 81:
        student_grades[student] = "exceed expectations"
    elif score >= 71:
        student_grades[student] = "acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)

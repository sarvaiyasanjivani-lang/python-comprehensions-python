students = [
    {"name": "Amit", "marks": [80, 90, 85]},
    {"name": "Ravi", "marks": [60, 70, 65]},
    {"name": "Priya", "marks": [95, 92, 98]},
]

student_averages = {
    student["name"]: sum(student["marks"]) / len(student["marks"])
    for student in students
    if student["marks"]
}

top_students = {
    name: average
    for name, average in student_averages.items()
    if average >= 85
}

print("Averages:", student_averages)
print("Top students:", top_students)

names = ["Khushi", "Vishwa"]
marks = [84,98]

student_marks = {
    name: mark
    for name, mark in zip(names, marks)
}

print(student_marks)

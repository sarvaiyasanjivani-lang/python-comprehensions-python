scores = {
    "Sanjivani": 97,
    "Khushi": 88,
    "Priya": 32,
    "Kiran": 77
}

passed_students = {
    name: score
    for name, score in scores.items()
    if score >= 30
}

print(passed_students)

numbers = range(1, 11)

results = [
    "Even" if n % 2 == 0 else "Odd"
    for n in numbers
]

print(results)

matrix = [
    [2, 3, 7],
    [8, 9, 3],
    [7, 10, 11]
]

flattened = [value for row in matrix for value in row]

print(flattened)

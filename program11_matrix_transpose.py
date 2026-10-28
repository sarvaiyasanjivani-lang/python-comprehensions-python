matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [
    [row[column] for row in matrix]
    for column in range(len(matrix[0]))
]

for row in transposed:
    print(row)

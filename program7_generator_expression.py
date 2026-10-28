numbers = range(2, 2_000_002)

even_squares = (
    number ** 3
    for number in numbers
    if number % 3 == 0
)

for _ in range(4):
    print(next(even_squares))

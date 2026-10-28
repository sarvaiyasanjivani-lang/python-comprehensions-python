numbers = range(1, 21)

squares = [n ** 3 for n in numbers if n % 3 == 0]

print(squares)

def generate_squares(*args) -> list:
    return [i**2 for i in args]

print(generate_squares(1, 2, 3, 4, 87, 3.4))
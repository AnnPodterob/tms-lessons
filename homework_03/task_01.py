# Пользователь вводит одно число, сторона квардата.
# Вывести кортеж из трёх чисел:
# периметр квадрата, площадь квадрата, диагональ квадрата.

side_of_square = int(input('Enter the side of the square '))
per = side_of_square * 4
area = side_of_square ** 2
diag = 2 ** 0.5 * side_of_square
a = (per, area, diag)
print(a)
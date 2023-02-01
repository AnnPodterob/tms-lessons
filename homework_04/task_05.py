# Пользователь вводит произвольное число.
# Посчитайте сумму цифр этого числа используя операторы % и //

n = int(input())
summa = 0
while n > 0:
    digit = n % 10
    summa = summa + digit
    n = n // 10
print(summa)

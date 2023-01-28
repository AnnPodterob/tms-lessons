# Пользователь вводит число, выведите True если оно простое, иначе False.

a = int(input("Enter number: "))
k = 0
for i in range(2, a // 2 + 1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("True")
else:
    print("False")

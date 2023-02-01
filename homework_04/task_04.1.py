# Программа загадывает случайное число от 0 до 100.
# Пользователь пытается угадать, вводя числа.
# Если пользователь угадал - выведите поздравление и завершите программу.
# Если пользователь не угадал, подскажите ему в в какую сторону идти.
# То есть, если число пользователя слишком большое - выведите “не угадал,
# ваше число больше загаданного”. Если меньше - выведите “не угадал,
# ваше число меньше загаданного”.

import random

num_to_guess = random.randint(0, 100)
while True:
    user_num = int(input('Enter a number: '))
    if user_num == num_to_guess:
        print('Congratulation!')
        break
    elif user_num < num_to_guess:
        print('Did not guess, your number is less than expected ')
    else:
        print('Did not guess, your number is higher')
# (Немного изменила условие, чтобы учесть количество попыток угадывания.
# Программа будет "помогать" пользователю до тех пор, пока количество попыток
# будет меньше 15, иначе она попросит повторить попытку. Подумала так интереснее)

import random

guesses_made = 0

num_to_guess = random.randint(0, 100)

while guesses_made < 15:
    user_guess = int(input('Enter the number '))
    guesses_made += 1
    if user_guess < num_to_guess:
        print('Did not guess, your number is less than expected ')
    if user_guess > num_to_guess:
        print('Did not guess, your number is higher')
    if user_guess == num_to_guess:
        break

if num_to_guess == user_guess:
    print('Congratulations! You guessed the number. You used {0} tries '.format(guesses_made))
else:
    print('You did not guess right. Try again ')

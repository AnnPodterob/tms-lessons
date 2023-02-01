# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
# Если он ответил “yes” - завершите программу.
# Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you"
# и продолжайте спрашивать до тех пор, пока ответ не будет корректным.

for i in range(0, 101):
    print(i)
    answer = input('Should we break? ')
    if answer == 'yes':
        break
    while answer != 'yes' and answer != 'no':
        answer = input('Dont understand you ')
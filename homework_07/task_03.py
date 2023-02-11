# Решите прошлую задачу, в которой теперь пользователь может вводить
# буквы в любом регистре. Вам по прежнему нужно удалить все гласные.
# При этом вывести результат нужно вывести сохранив изначальный регистр.

def new_remove_vowels(vowels_list: list):
    none_letters = ['a', 'o', 'i', 'u', 'e']
    new_list_letters = list(filter(lambda x: x not in none_letters, vowels_list))
    return new_list_letters

user_letters = input('Enter letters separated by spaces: ').split()
print(new_remove_vowels(user_letters))
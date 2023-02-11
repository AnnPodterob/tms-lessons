# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих
# букв и удаляет из него все гласные буквы. Выведите результат работы на экран.

def remove_vowels(vowels_list: list):
    none_list = ['a', 'e', 'i', 'o', 'u']
    new_list = list(filter(lambda x: x not in none_list, vowels_list))
    return new_list

user_letters = input('Enter letters separated by spaces: ').lower().split()
print(remove_vowels(user_letters))
# Пользователь вводит произвольное количество слов через пробел.
# Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join, которая принимает список из
# строк и символ-разделить, и возвращает строку, в которой все слова
# из списка соединены через символ разделитель.

from functools import reduce

user_str = input('Enter words separated by spaces: ').split()
user_separator = input('Enter a separator character: ')

def my_join(str_list: list, sep) -> str:
    new_str = reduce(lambda x, y: x + sep + y, str_list)
    return new_str

print(my_join(user_str, user_separator))
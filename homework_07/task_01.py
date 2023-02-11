# Пользователь вводит произвольное количество латинских букв
# через пробел. Буквы могут быть как в верхнем, так и в нижнем
# регистре (на результат работы это влиять не должно).
# Напишите функцию map_to_tuples, которая принимает список из этих
# букв и возвращает список из кортежей. В каждом кортеже первой
# должна идти буква в верхнем регистре, а второй эта же буква в нижнем.
# Выведите результат работы функции на экран.

def map_to_tuples(letters_list: list) -> list[tuple]:
    new_letters_list = list(map(lambda letter: (letter.upper(), letter.lower()), letters_list))
    return new_letters_list

user_letters = input('').split()
print(map_to_tuples(user_letters))
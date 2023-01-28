# Пользователь вводит произвольную строку.
# Выведите кортеж из уникальных символов введённой строки.

y_str = input()
uniq_symbols = set(y_str)
a = tuple(uniq_symbols)

print(a)

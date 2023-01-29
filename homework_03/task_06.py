# Пользователь вводит месяц и число. Выведите True, если такой день есть в году.

x = input('Enter the month ')
y = int(input('Enter the day of month '))

year = {
 'January': range(1, 31),
 'February': range(1, 28),
 'March': range(1, 31),
 'April': range(1, 30),
 'May': range(1, 31),
 'June': range(1, 30),
 'July': range(1, 31),
 'August': range(1, 31),
 'September': range(1, 30),
 'October': range(1, 31),
 'November': range(1, 30),
 'December': range(1, 31)
}

date_of_the_year = year[x]
print(x in year and y in date_of_the_year)
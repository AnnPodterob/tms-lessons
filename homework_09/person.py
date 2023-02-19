# Создайте файл person.py, делайте задание в этом файле.
# Создайте класс Person. У класса должно быть три поля: full_name,
# age, gender, которые должны заполняться в конструкторе. Будем считать
# что поле gender имеет тип str и может быть либо 'M' (male), либо 'F' (female).
# Добавьте в класс метод print_person_info, который печатает на экран строку:
# "Person: {full_name} ({gender}), {age} years old"
# Добавьте метод get_birth_year, которая возвращает год рождения человека (рассчитанное как 2023 - age)
# * Замените цифру 2023 на текущий год (чтобы ваша программа работала правильно
# даже через год). Текущий год можно взять с помощью модуля datetime

import datetime

now = datetime.datetime.now()

class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        full_name = self.full_name
        gender = self.gender
        age = self.age
        print(f'Person: {full_name} ({gender}), {age} years old')

    def get_dirth_year(self):
        return now.year - self.age

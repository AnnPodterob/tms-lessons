import sqlite3
import re


def is_phone_number(s: str) -> bool:
    return re.fullmatch(r'\+375 \((29|25|33|44)\)\d{3}-\d{2}-\d{2}', s) is not None

def is_correct_input(s: str) -> bool:
    return re.fullmatch(r'[А-Яа-яA-Za-z]+', s) is not None

def is_correct_initials(s: str) -> bool:
    return re.fullmatch(r'[A-ZА-Я][A-ZА-Я][A-ZА-Я]', s) is not None


class PhoneBook:
    def __init__(self):
        with sqlite3.connect('sqlite.db') as connection:
            connection.execute('create table if not exists myphonebook ( id INTEGER PRIMARY KEY AUTOINCREMENT, '
                               'name VARCHAR, initials VARCHAR, phone_number VARCHAR, place_of_residence VARCHAR)')


    def add_cont(self, name, initials, phone_number, place_of_residence):
        new_cont = (name, initials, phone_number, place_of_residence)
        with sqlite3.connect('sqlite.db') as connections:
            connections.execute('insert into phonebook (name, initials, phone_number, '
                                        'place_of_residence) values (?,?,?,?)', new_cont)

    def alf_cont(self):
        with sqlite3.connect('sqlite.db') as connection:
            result = connection.execute('SELECT * FROM phonebook order by name')
            for phone in result.fetchall():
                print(phone)

    def update_cont(self, name, phone_number):
        new_phone = (name, phone_number)
        with sqlite3.connect('sqlite.db') as connection:
            connection.execute('update phonebook set phone_number = ? where name = ?', new_phone)


class Controller:
    def __init__(self):
        self.phone_book = PhoneBook()

    def run(self):
        print('Добро пожаловать в нашу телефонную книгу!')
        while True:
            print('Выберите действие:')
            print('0. Выйти из программы')
            print('1. Добавить новый контакт')
            print('2. Вывести весь список контактов в алфавитном порядке')
            print('3. Обновить номер контакта')
            act = int(input())
            if act == 0:
                print("До свидания!")
                break

            elif act == 1:
                print('Добавление нового контакта')
                name = str(input('Введите имя нового контакта (последовательно, фамилию имя отчество): '))

                if is_correct_input(name) is False:
                    print('Введите Фамилию Имя и Отчетсво корректно! ')
                    name = str(input('Введите имя нового контакта (последовательно, фамилию имя отчество): '))

                initials = str(input('Введите инициалы нового контакта: '))

                if is_correct_initials(initials) is False:
                    print('Введите инициалы корректно!')
                    initials = str(input('Введите инициалы нового контакта ещё раз: '))

                phone_number = str(input('Введите номер телефона, соответсвующий стандартному шаблону: '))

                if is_phone_number(phone_number) is False:
                    print('Введите номер КОРРЕКТНО. Например: +375(29)391-26-61')
                    phone_number = str(input('Введите номер телефона, соответсвующий стандартному шаблону: '))

                place_of_residence = str(input('Введите место жительства нового контакта: '))

                if is_correct_input(name) is False:
                    print('Введите Место жительства корректно! ')
                    place_of_residence = str(input('Введите место жительства нового контакта: '))

                self.phone_book.add_cont(name, initials, phone_number, place_of_residence)
                print('Контакт добавлен!')

            elif act == 2:
                print('Модернизация списка контактов в алфавитном порядке')
                self.phone_book.alf_cont()

            elif act == 3:
                print('Обновление номера контакта')
                name = str(input('Введите имя нового контакта (последовательно, фамилию имя отчество): '))

                if is_correct_input(name) is False:
                    print('Введите Фамилию Имя и Отчетсво корректно! ')
                    name = str(input('Введите имя нового контакта (последовательно, фамилию имя отчество): '))

                phone_number = str(input('Введите новый номер телефона контакта: '))

                if is_phone_number(phone_number) is False:
                    print('Введите номер КОРРЕКТНО. Например: +375(29)391-26-61')
                    phone_number = str(input('Введите номер телефона, соответсвующий стандартному шаблону: '))

                self.phone_book.update_cont(name, phone_number)
                print('Контакт обновлён')


if __name__ == '__main__':
    control = Controller()
    control.run()


# Создайте файл university.py. Делайте задание в этом файле.
# Импортируйте класс Student из первого задания
# from student import Student
# Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
# Посчитайте суммарную стипендию для всех студентов.
# Посчитайте количество отличников (используйте метод is_excellent).
# * Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count

from student import Student

students = [
    Student('Ivan Ivanov', 8.3),
    Student('Anatoly Kovchic', 9.3),
    Student('Petr Petrov', 5.6),
    Student('Anya', 9.6)
]

def calc_sum_scholarship():
    sum = students[0].get_scholarship()
    for i in students[1:]:
        sum += i.get_scholarship()
    return sum

def get_excellent_student_count():
    k = 0
    for i in students:
        if i.is_excellent() is True:
            k += 1
    return k


print(calc_sum_scholarship())
print(get_excellent_student_count())
# coding=utf-8
# Пример работы с list
# Создание
my_list = []
# my_list = list()

# Добавление элементов
my_list.append(1)  # добавление одного элемента
my_list.extend([2, 3, 4])  # Обьединение двух списков
print my_list + [2, 3, 4, 5]  # Обьединение двух списков. В отличий от пред. не изменяется исходный вариант
print my_list
my_list.insert(0, 0)  # Вставка по индексу
print my_list

# Изменение элементов
my_list[0] = -1
print my_list
my_list[0:2] = [9, 10]
print my_list

# Удаление элементов
del my_list[0]
# del  my_list  # Удаляет весь список
print my_list
my_list.remove(4)  # удаление элемента 4
my_list.pop(0)  # Удаление по индексу. По умолчанию -1

# Работа со списком
# В цикле
for i in my_list:
    print i

# Условие
if 3 in my_list:
    print "3 is in my_list"
else:
    print "3 is not in my_list"

# Лист умеет хранить разные обьекты
print [1, "abc", ArithmeticError]
print my_list * 5  # Можно умножать на цифру

my_list = [x for x in xrange(100)]

# брать срез
print my_list[0:10]

print my_list[::-1]
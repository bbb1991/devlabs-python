# coding=utf-8
# Пример работы с tuple
# создание
my_tuple = (1, 2,)
print type(my_tuple)

print tuple("python")

# Работа с кортежами
print my_tuple + (3, 4, 5)

for i in my_tuple:
    print i

print my_tuple.count(2)  # Сколько раз содержится элемент 2 в кортеже

a, b, c = (1, 2, 3)  # Распаковка
print a, b, c

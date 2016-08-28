# coding=utf-8
"""
Работа с функциями.
"""


# Простая функция
def multiple(a, b):
    return a * b


# Функция с аргументами по умолчанию
def divide(a=2, b=1):
    if b == 0:
        return
    return float(a / b)


# Функция с неизвестным количеством аргументов
def summirize(a, b=8, *args):
    s = a + b
    for arg in args:
        s += arg
    return s

print(multiple(2, 2))
print(divide(b=2))
print(summirize(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
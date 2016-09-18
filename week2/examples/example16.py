# coding=utf-8
# пример импорта. Импорт функций, классов, переменных из модуля
from os import path  # импорт функций
from os import environ as ENV  # импорт с переименованием

print(path.realpath(__file__))
print(ENV)
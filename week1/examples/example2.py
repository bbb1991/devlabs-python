# coding=utf-8
"""
Пример изменяемых и неизменяемых типов данных.
"""

b = 5
print id(b)
b += 1
print id(b)

a = ['a', 'b', 'c']
print id(a)
a.append('d')
print id(a)

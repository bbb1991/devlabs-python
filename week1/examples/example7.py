# coding=utf-8
"""
Циклы. While
while ___:
    code
"""

i = -1
while True:
    i += 1
    if i == 100:
        break
    if i % 2 != 0:
        continue
    print(i)

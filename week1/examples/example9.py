# coding=utf-8
"""
Работа с файлами
"""

f = open("file1.txt", "w")

for i in range(100):
    f.write(str(i) + " ")
f.close()

f = open("file1.txt")
for item in f.readlines():
    print(item)

f.close()
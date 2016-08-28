# coding=utf-8
"""
Условные операторы
"""

user_input = int(input("Please, input integer -10..10: "))

if user_input > 0:
    print("You entered positive number")
elif user_input < 0:
    print("You entered negative number")
else:
    print("It's 0!!!")

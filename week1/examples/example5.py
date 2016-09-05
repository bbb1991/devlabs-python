# coding=utf-8
"""
Условные операторы

if ___:
    code...
elif ___:
    code...
else:
    code...

"""

username = raw_input("Enter your login: ")
password = raw_input("Enter your password: ")

if username == "admin" and password == "admin":
    print("Welcome, admin")
elif username == "guest" or password == "guest":
    print("Welcome, guest!")
else:
    print("Go away, hacker!")

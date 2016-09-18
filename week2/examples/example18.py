# coding=utf-8
# Разное


# Укороченная запись if else
def my_abs(x):
    return x if x >= 0 else x * -1


print(my_abs(-5))

# Печать подключенных модулей
print(dir(__builtins__))

# аналог type()
print(isinstance(1, int))

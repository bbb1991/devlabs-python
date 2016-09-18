# coding=utf-8
# Пример работы с dict

# Создание
my_dict = {1: "a", 666: "zzz"}
# my_dict = dict(1=1)
print(dict.fromkeys("abc"))  # Создание словаря с переданными ключами и дефолтным значением.

# Добавление
my_dict[2] = "b"
print(my_dict)

# Удаление
del my_dict[2]  # Удаление по ключу
print(my_dict)

my_dict.pop(1)  # Удаляет из словаря и возвращает значение
print(my_dict)

my_dict.popitem()  # Удаляет из словаря случайный элемент и возвращает значение

# Изменение
my_dict = {1: "a", 2: "b", 3: "c"}
my_dict[1] = "z" # по индексу
my_dict.update({1: 100}) # Вызовом функций
print(my_dict)

# Работа со словарями
# Проход с циклом по ключу/значению
for key, value in my_dict.items():
    print(key, value)

# Проход по циклу по ключу
for key in my_dict.keys():
    print ("Key is:", key, "and value is:", my_dict[key])

# Проход по ключу по значению
for value in my_dict.values():
    print(value)

print(my_dict.has_key("x")) # Есть ли данный ключ в словаре
# Хотя рекомендуется следующая запись
print('x' in my_dict)


# Получение значений по ключу
print(my_dict[1])
# или так
print(my_dict.get(1))
# Различие в том что при обращений по индексу если такого ключа нет, будет ошибка, а get() вернет None


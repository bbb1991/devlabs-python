# coding=utf-8
# Пример работы с set
# Set - структура данных, который не хранит дубли
my_set = {1, 1, 1, 1, 1, 1, 3}
print my_set
# добавление
my_set.add(5)  # Добавление элемента
my_set.update({10, 20, 30})  # Добавление множества
print my_set

# Изменение

# Удаление
my_set.discard(10)  # Удаление элемента
my_set.remove(1)
print my_set

my_set.difference_update({1, 2, 3})  # Удаление элементов, которые есть во обоих множествах
print my_set
# my_set -= {1, 2, 3} # или так


# Работа с set
print my_set.difference({20, 30})  # Возвращает разницу
print my_set - {20, 30}

print my_set.intersection({20, 30})  # Возвращает элементы, которые есть в обоих множествах
print my_set & {20, 30}

print my_set.union({-1, -2, -3}) # обьединение двух множеств
print my_set | {-1, -2, -3}


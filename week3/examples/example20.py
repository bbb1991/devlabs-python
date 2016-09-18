class Student:
    address = "Tharsis, Mars"

    # Constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return "Student name is: " + self.name + ", year is " + str(self.year) + ", and address is: " + self.address

    def __del__(self):
        print("deleting student 1")


student1 = Student("Smith", 2010)
print(student1)

student2 = Student("Doe", 2012)
student2.address = "Astana, Kazakhstan"
print(student2)
print(student1)
del student1

# Динамическое добавление атрибутов
student2.is_alive = True
print(student2.is_alive)
print(student1.is_alive)
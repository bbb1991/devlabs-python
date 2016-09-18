class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return "Person name is: %s" % self.name


class Student(Person):
    def __init__(self, group, name):
        Person.__init__(self, name)
        self.group = group

    def info(self):
        return "Student name is: %s and group is: %d" % (self.name, self.group)

vasya = Person("Vasya")
print(vasya.info())
print(Person.info(vasya))

petya = Student(25, "Petya")
print(petya.info())
print(Student)

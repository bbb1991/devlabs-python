from random import random


class RandomGen:
    def __init__(self):
        self.counter =0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == 10:
            raise StopIteration
        self.counter += 1
        return random()

for i in "asdsad":
    print(i)


it = iter("abcd")
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())


class A:


    def __init__(self):
        self.l = [1, 2, 3, 4]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1
        return self.l[self.index]


a = A()
for i in a:
    print(i)
    
it3 = iter(a)

r = RandomGen()

it2 = iter(r)
print(it2.__next__())
print(it2.__next__())
print(it2.__next__())
print(it2.__next__())

for i in r:
    print(i)

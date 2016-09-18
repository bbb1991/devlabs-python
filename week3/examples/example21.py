# static attr example


class Counter:
    counter = 0

    def __init__(self):
        self.__class__.counter += 1

    def __str__(self):
        return "static counter: %d and non static counter" % self.__class__.counter


a = Counter()
b = Counter()
c = Counter()

print(Counter.counter)

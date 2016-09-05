# Recursive call example:


def fib(index=1):
    if index == 1 or index == 2:
        return 1
    if index == 0:
        return 0
    return fib(index - 1) + fib(index - 2)


n = int(raw_input("Please, input n: "))
print fib(n)

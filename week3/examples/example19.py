# Определение класса.
# class <ClassName>(ParentClass1, ParentClass2):
# ... code


class A:
    """Useless class example."""
    var1 = 12345

    def foo(self):
        """
        method that doing nothing
        :return: None
        """
        pass


a = A
print(a.var1)
print(A.__doc__)


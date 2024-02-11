class Foo():

    def __init__(self):
        self.__one = 1
        self.__two = 2
        self.__three = 3

    def foo_def(self, a):
        if type(a) == int:
            self.__one = 1
            self.__two = 2
            self.__three = 3
        else:
            self.__one = 'one'
            self.__two = 'two'
            self.__three = 'three'

    def get_self(self):
        return (self.__one, self.__two, self.__three)

example = Foo()
a, b = 1, 'one'
print(example.get_self())

example.foo_def(a)
print(example.get_self())

example.foo_def(b)
print(example.get_self())

example.foo_def(a)
print(example.get_self())

class Bye:
    def __init__(self):
        self.foo = 'bar'

    def is_hello(self):
        return type(self) == Hello

class Hello:
    def __init__(self):
        self.value = 'foobar'

print(Bye().is_hello())



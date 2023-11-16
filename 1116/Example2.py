class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name:{self.name} Age={self.age}"

    def myfunc(self):
        print(self.name, "is tt")

p1 = Person("John", 36)
p2 = Person("Xi WeiNe", 64)
print(p1)
print(p2)
p1.myfunc()
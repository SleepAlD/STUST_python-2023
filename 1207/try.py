class fruit :
    def __init__(self, name) :
        self.name = name

    @property
    def fruit_name(self):
        print(f"{self.name} is good\n")
        return self.name

    @fruit_name.setter
    def fruit_name(self, value):
        print(f"{self.name} is become {value}\n")
        self.name = value

    @fruit_name.deleter
    def fruit_name(self) :
        print(f"{self.name} was dead\n")
        del self.name


Fruit = fruit('Apple')
Fruit.fruit_name

Fruit.fruit_name = 'Banana'
Fruit.fruit_name

del Fruit.fruit_name
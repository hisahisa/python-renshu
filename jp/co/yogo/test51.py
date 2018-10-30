class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name + ":" + str(self.age)

#    def __str__(self):
#        return "<Name:{}, Age:{}>".format(self.name, self.age)

john = Person("John", 38)
luice = Person("Luice", 32)
print(john)
print(luice)


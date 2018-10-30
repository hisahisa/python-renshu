"""

"""

class Dog:
    def __init__(self, name, bredd, owner):
        self.name = name
        self.breed = bredd
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick jagger")
stan = Dog("stanley", "boodle", mick)
print(stan.owner.name)

mic2 = Person("Michael jacson")
sta2 = Dog("goophyee", "poodle", mic2)
print(sta2.owner.name)
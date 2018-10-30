class Coodinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord: " + str(self.__dict__)


def add(a, b):
    return Coodinate(a.x + b.x, a.y + b.y)


def sub(a, b):
    return Coodinate(a.x - b.x, a.y - b.y)


def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coodinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coodinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coodinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker

one = Coodinate(100, 200)
two = Coodinate(300, 200)
three = Coodinate(-100, -100)

add = wrapper(add)
sub = wrapper(sub)
print(sub(one, two))
print(add(one, three))



# one = Coodinate(100, 200)
# two = Coodinate(300, 200)
# three = Coodinate(-100, -100)
#
# print(sub(one, two))
# print(add(one, three))



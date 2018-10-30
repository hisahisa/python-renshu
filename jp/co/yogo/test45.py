# print(issubclass(int , object))
#
#
# def foo():
#     pass
#
#
# print(foo.__class__)
#
#
# print(issubclass(foo.__class__, object))


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def apply(func, x, y):
    return func(x, y)


print(apply(add, 3, 4))
print(apply(sub, 3, 4))







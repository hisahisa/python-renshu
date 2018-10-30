
def outer(x):

    def inner():
        print(x)
    return inner


foo = outer('yogo')
print(foo.__closure__)


print1 = outer(1)
print2 = outer(2)

print1()
print2()


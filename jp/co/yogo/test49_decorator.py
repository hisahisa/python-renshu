def outer(some_func):

    def inner():
        print('before some func')
        ret = some_func()
        return ret + 1
    return inner


def foo():
    return 1


decorated = outer(foo)
ret = decorated()
print(ret)

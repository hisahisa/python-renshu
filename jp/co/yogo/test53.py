"""
他のクラスのデコレーターをメソッドから呼び出しに成功したケース
"""

from test52 import LoggerClass


# def logger(func):
#    def inner(*args, **kwargs):
#        print("Arguments were : %s, %s" % (args, kwargs))
#        return func(*args, **kwargs)
#    return inner


# class LoggerClass(object):

foo = LoggerClass()


@foo.logger
def foo1(*x, **y):
    print(x)
    print(x[0])
    print(y)
    return x[0] * y['y']


# l = LoggerClass()

print(foo1(5, 1, 8, x=6, y=8))

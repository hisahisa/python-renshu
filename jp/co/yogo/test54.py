"""
他のクラスのデコレーターをクラスのメソッドから呼び出しに成功したケース
"""
from test52 import LoggerClass


class NanchatteLoggerClass(object):
    foo = LoggerClass()

    @foo.logger
    def foo1(self, *x, **y):
        print(x)
        print(x[0])
        print(y)
        return x[0] * y['y']


log = NanchatteLoggerClass()
print(log.foo1(5, 1, 8, x=6, y=8))

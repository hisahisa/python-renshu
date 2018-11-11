def coro1(st):
    hello = yield "Hello {}".format(st)
    yield hello
    yield from coro1(st)


def coro():
    hello = yield "Hello"
    val = ""
    val = yield hello + val

c = coro()
print(next(c))
print(c.send("World"))


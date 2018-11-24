def coro1(st):
    i = 0
    while 1:
        hello = yield "Hello {}".format(st)
        yield hello
        yield from coro1(st)

def coro():
    x = 0
    while 1:
        if x == 10:
            raise StopIteration
        else:
            hello = yield "Hello"
            x += 1
            yield hello

c = coro()
#c = coro1("wo")

for i in c:
    print(i)


# x = next(c)
# print(x)
# print('--')
#
# x = next(c)
# print(x)
# print('--')
#
# x = next(c)
# print(x)
# print('--')
#
# x = next(c)
# print(x)
# print('--')
#
# x = next(c)
# print(x)
# print('--')

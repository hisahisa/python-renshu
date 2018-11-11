def coroutine():
    for i in range(1, 10):
        print("From generator {}".format((yield i)))
c = coroutine()
c.send(None)
try:
    while True:
        print("From user {}".format(c.send(5)))
except StopIteration: pass
def generator(step):
    val = 0
    prev = 0
    while True:
        if step is None:
            step = prev
        prev = step
        val += step
        step = yield val


if __name__ == '__main__':
    gen = generator(0)

    print(dir(gen))

    print(gen.__next__(), end=' ')
    for i in [1, 2, 3, 4, 5, 6]:
        print(gen.send(i), end=', ')
    print()

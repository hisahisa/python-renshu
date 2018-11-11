# リスト
def accum_list(iterable):
    current = 0
    lst = []
    for elem in iterable:
        current += elem
        lst.append(current)
    return lst


# ジェネレーター
def accum_gen(iterable):
    current = 0
    for elem in iterable:
        current += elem
        v = yield current

def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1

ite = 1,2,3,5

print(accum_list(ite))

ret = accum_gen(ite)
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))


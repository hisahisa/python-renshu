def ex_permutation(iterable, now_list=[]):
    if not iterable:
        yield now_list
        return
    a = [iterable.index(ite_x) for ite_x in set(iterable)]
    #a = {ite_x for ite_x in set({'a':1,'b':2,'a':3})}
    for arr_x in a:
        i = iterable[:arr_x] + iterable[arr_x + 1:]
        r = now_list + [iterable[arr_x]]
        yield from ex_permutation(iterable[:arr_x] + iterable[arr_x + 1:], now_list + [iterable[arr_x]])


if __name__ == '__main__':
    #permu = ex_permutation({'a':1,'b':2,'a':3})
    permu = ex_permutation([1,2,1])
    for i in permu:
        print(i)

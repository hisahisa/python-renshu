import sys

sys.setrecursionlimit(10000)


def multi5(n):
    m = 5
    if n == 0:
        return 0
    else:
        return multi5(n - 1) + m


n = int(input("input n = "))
print('5 x', n, ' = ', multi5(n))

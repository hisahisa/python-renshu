import numpy as np
import re


def custom_filter(n):
    #pattern = '\\s+'
    pattern = '\S+ '
    repatter = re.compile(pattern)

    #if repatter.match(n[0]):
    #return n[0].split(' '))
    print(n[0])
    print(type(n[0]))
    #x = re.sub('\s+', " ", n[0]).strip()
    return re.sub( '\s+', ' ', n[0] ).strip()
    #else:
    #    return n[0]


# Driver function
if __name__ == "__main__":
    #l1 = [(7, 2), (3, 4), (5, 5), (10, 3)]
    l1 = [("Beal saes", 2), ("Bea  tles", 4), ("Bea       tis", 5), ("Beui", 3)]

    print("res = ", list(map(custom_filter, l1)))


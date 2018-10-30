def add(x, y):
    """
    Return x + y.
    :param x: int.
    :param y: int.
    :return: int sum of x and y
    """
    print(x + y)
    x = int(input("input num:"))
    y = int(input("input another:"))
    add(x, y)


a = int(input("input num:"))
b = int(input("input another:"))
print(add(a, b))

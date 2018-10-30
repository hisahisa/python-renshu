
#def sum_(x, y):
#    return x + y


# これをカリー化すると↓
def add_x(x):
    return lambda y: x + y


curry_sum = add_x(10)
print(curry_sum)
print(dir(curry_sum))

print('----------------')
print(dir(curry_sum.__closure__[0]))
print(curry_sum.__closure__[0].cell_contents)
print('----------------')

print(curry_sum(20))


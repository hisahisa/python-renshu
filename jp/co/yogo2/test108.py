
from numpy import *

def f(x):
    return sin(pi*x)

n = 1000000
product = prod( [sum((1/n) * f(k/n)**m for k in range(n)) for m in range(1, 11)] )
result = 1.0/product
print(result)


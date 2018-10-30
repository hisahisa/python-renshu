
l1 = [2,'j',5]

try:
    l2 = map(lambda x: x ** 2, l1)
    print(list(l2))
except ValueError:
    print("sorry")

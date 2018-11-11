
def gen(init_val):
    print("init_val=", init_val)
    val = init_val
    step = 0
    while True:
        print("val=", val)
        print("step=", step)
        val = val + step
        step = yield val

print("---gen(3)呼び出し---")
g = gen(3)

print("---g.__next__()呼び出し---")
print( g.__next__() )
print("---")

print("---g.send(10)呼び出し---")
print( g.send(10) )
print("---")

print("---g.send(5)呼び出し---")
print( g.send(5) )
print("---")

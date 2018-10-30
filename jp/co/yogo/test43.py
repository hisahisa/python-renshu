
def foo(arg):
    x = 10
    print(locals())

    for k,v in globals().items():
        print('{},: {}'.format(k , v))


# text = 'I am global!'
# def foo2():
#     text = 'I am local!'
#     print(text)
#
# foo2()
#
# print(text)

def foo():
    x = 1

foo()
print(x)


def sample():
    a = int(input("input num:"))
    b = int(input("input another:"))

    try:
        print(a / b)
        sample()
    except ZeroDivisionError:
        print("a nother cannot be zero")
        sample()
    except ValueError:
        print('Value cannot be zero')
        sample()


sample()

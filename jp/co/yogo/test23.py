
class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n + -30)


x = AlwaysPositive(23)
y = AlwaysPositive(-10)

print(x + y)


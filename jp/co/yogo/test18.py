"""
ポリもーフィズムなし
"""


class Figure:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def draw(self):
        print("print w is {}".format(self.width))
        print("print h is {}".format(self.height))


class Triangle(Figure):
    pass


#    def __init__(self, w, h):
#        super().__init__(w, h)

class Square(Figure):
    pass


#    def __init__(self, w, h):
#        super().__init__(w, h)


class Circle(Figure):
    pass


#    def __init__(self, w, h):
#        super().__init__(w, h)

tr1 = Triangle(100, 102)
sq1 = Square(200, 201)
cr1 = Circle(300, 301)

shapes = [tr1, sq1, cr1]

for a_shape in shapes:
    if isinstance(a_shape, Triangle):
        a_shape.draw()
    if isinstance(a_shape, Square):
        a_shape.draw()
    if isinstance(a_shape, Circle):
        a_shape.draw()

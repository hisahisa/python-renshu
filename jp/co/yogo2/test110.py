
class y110(object):
    def __init__(self, a):
        self.x = a
        #self.y = b

    def __str__(self):
        return "{self.__class__.__name__}({self.a}, {self.b})".format(self=self)

    def xyz(self):
        return 1
    def incheck(self, f):

        for k,v in dict.items():
            print("k,v = {},{}".format([k,v]))


        if isinstance(f, dict):
            return 1
        else:
            return 2

def xx():
    return 'x'







class Orange:
    def __init__(self, w, c):
        """weight (重さ) はグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!!!")

    def rot(self, days, temp):
        """temp(温度)は摂氏"""
        self.mold = days * temp

ora = Orange(200, "orange")
print(ora.mold)
ora.rot(10, 37)
print(ora.mold)

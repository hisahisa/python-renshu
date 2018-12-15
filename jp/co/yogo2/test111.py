
class test111:

    def testdef2(self, dict_list):
        print(list(map(self.one_testdef3, dict_list.items())))
            #print("%s : %s" % (number, divide))

    def one_testdef3(self, x, y):
       return (x, y)

    def testdef(self, number_list):
        for number, divide in zip(number_list, map(self.one_divide_by, number_list)):
            print("%d : %f" % (number, divide))

    def one_divide_by(self, n):
        try:
            return 1/n
        except ZeroDivisionError:
            return 0   #or some other default value.

number_list = [1,2,4,0,5]
#number_list = {"a":1,"b":2,"c":4,"d":0,"e":5}
t111 = test111()
t111.testdef(number_list)
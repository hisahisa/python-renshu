import numpy as np

arr = np.asarray([[1,2,3],[4,5,6]])

b = map(lambda x :map(lambda a: a + 1, arr), arr)





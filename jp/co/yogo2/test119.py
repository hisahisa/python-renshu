
import pandas
import pickle
import redis

from time import time

HEADER = ['yahoo','amazon','google']


def testx():
    csv = pandas.read_csv('/Users/yogohisashi/yogodev/KEN_ALL.CSV', encoding='shift-jis',
                          usecols=(0,1,2), names=HEADER, chunksize=10000)

    # バイト列をファイルにダンプ
    #    dumped = pickle.dumps(csv, protocol=2)

    #    r = redis.Redis(host='localhost', port=6379, db=0)
    #    r.set('usdjpy-1m.csv', dumped)

    n=100
    #    csv = pickle.loads(r.get('usdjpy-1m.csv'))
    for i in csv:
        yield i


def testx2():
    i = testx()
    for df in i:

        #X = ["0", "1", "2", "3"]
        #Y = ["100", "200", "300"]
        #n = []
        #t = list(map(lambda x: list(map(lambda y: x + y, Y)),X))

        Y = range(0, 10)
        X = df.columns.values.tolist()
        n = []
        t = map(lambda x: dict(map(lambda y: { x, y}, Y)), X)

        print(list(t))

#        insert_dict_data = [dict(r = df.iat[i, HEADER.index(r)] for r in df.columns.values.tolist() ) for i in range(0, df.shape[0])]
        #map(lambda x: n.extend(map(x, [100, 200, 300])), map(lambda x: lambda y: x + y, [0, 1, 2]))
        # insert_dict_data = map(lambda df: range(0, df.shape[0]))
        a = [[1, 2, 3], [7, 8, 6]]
        #insert_dict_data = map(lambda i: list(map(lambda r: dict(r =  df.iat[i, HEADER.index(r)] ,  df.columns.values.tolist() ))), range(0, df.shape[0]))
        #insert_dict_data = map(lambda i: list(map(lambda r: {r: df.iat[i, HEADER.index(r)] },  df.columns.values.tolist())), range(0, df.shape[0]))
        #insert_dict_data =   map(lambda i: list(map(lambda j: j - 1, i)), a)
#        print(insert_dict_data)

testx2()



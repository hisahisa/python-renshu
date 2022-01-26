
import pandas


HEADER = ['yahoo','amazon','google']


def testx():
    csv = pandas.read_csv('/Users/yogohisashi/yogodev/KEN_ALL.CSV', encoding='shift-jis',
                          usecols=(0,1,2), names=HEADER, chunksize=100)
    for i in csv:
        yield i


def testx2():
    i = testx()
    for df in i:
        X = range(0, df.shape[0])  # [1,2,3 ]
        Y = df.columns.values.tolist() # ['yahoo','amazonl','google']
        t = map(lambda x: dict((y ,df.iat[x, HEADER.index(y)]) for y in Y), X)
        print(list(t))


# -- mixed renshu1

testx2()



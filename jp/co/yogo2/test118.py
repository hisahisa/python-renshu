
import pandas
import pickle
import redis

from time import time

def calctime(func):
    start = time()
    r = func()
    return {'value': r, 'time': time()-start}

def testx():
    csv = pandas.read_csv('/Users/yogohisashi/yogodev/KEN_ALL.CSV', encoding='shift-jis')

    # バイト列をファイルにダンプ
#    dumped = pickle.dumps(csv, protocol=2)

#    r = redis.Redis(host='localhost', port=6379, db=0)
#    r.set('usdjpy-1m.csv', dumped)

    n=10000
#    csv = pickle.loads(r.get('usdjpy-1m.csv'))
    for i in range(1, len(csv), n):
        print(csv[i: i+n])

ret = calctime(lambda : testx())
print('redisを使うと{}秒かかりました'.format(ret))


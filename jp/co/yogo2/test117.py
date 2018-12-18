
import pandas
import pickle
import redis


from time import time

def calctime(func):
    start = time()
    r = func()
    return {'value': r, 'time': time()-start}

# csvの読み込み
#csv = pandas.read_csv('/Users/yogohisashi/yogodev/KEN_ALL.CSV', parse_dates=['time'], index_col='time', encoding='shift-jis')
csv = pandas.read_csv('/Users/yogohisashi/yogodev/KEN_ALL.CSV', encoding='shift-jis')

# バイト列をファイルにダンプ
dumped = pickle.dumps(csv, protocol=2)

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('usdjpy-1m.csv', dumped)

# ダンプしたファイルを再度読み込み
csv = calctime(lambda: pickle.loads(r.get('usdjpy-1m.csv')))
print('redisを使うと{}秒かかりました'.format(csv))

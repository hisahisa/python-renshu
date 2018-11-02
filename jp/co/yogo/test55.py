import datetime
import collections as ct

import more_itertools as mit

data_i = [
    {"date": datetime.date(2013, 1, 1), "id": 99, "value1": 15},
    {"date": datetime.date(2013, 1, 1), "id": 99, "value1": 12, "value2": 14},
    {"date": datetime.date(2013, 1, 1), "id": 98, "value1": 13, "value2": 9},
    {"date": datetime.date(2013, 1, 2), "id": 97, "value1": 11, "value2": 7},
    {"date": datetime.date(2013, 1, 3), "id": 96, "value1": 10, "value2": 5},
    {"date": datetime.date(2013, 1, 4), "id": 95, "value1": 3, "value2": 4},
    {"date": datetime.date(2013, 1, 2), "id": 99, "value1": 14, "value2": 2}
]


#kfunc = lambda d: d["date"]
#vfunc = lambda d: {k:v for k,v in d.items() if k.startswith("val")}
#rfunc = lambda lst: sum((ct.Counter(d) for d in lst), ct.Counter())

def kfunc(d):
    # 集計のカテゴリを決めるみたいだな。。
    d_val = d["date"]
    #d_val = (d["date"],d["id"]) key複数の場合は tuple で渡してあげればok
    return d_val


def vfunc(d):
    # 集計値の定義をするらしいいいいい。。
    # val = {'val':v for k,v in d.items() if k.startswith("val")}  # value* で一括集計したい
    val = {k:v for k,v in d.items() if k.startswith("val")} # value1, value2 集計を仕分けする
    return val


def rfunc(lst):
    # reduce function 集約してくれるみだいだ。
    r_val = sum((ct.Counter(d) for d in lst), ct.Counter())
    return r_val


result = mit.map_reduce(data_i, keyfunc=kfunc, valuefunc=vfunc, reducefunc=rfunc)

for k,v in result.items():
    print(k)
    print(v)





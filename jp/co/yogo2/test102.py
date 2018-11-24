# 英小文字で構成された、ランダムな100文字を生成
import random
import string

import collections


n = 100
val_str = ''.join([random.choice(string.ascii_lowercase) for i in range(n)])
print(val_str)

c = collections.Counter(val_str)
print(c)

#d = {}
d = collections.defaultdict(int)
print(type(d))  # type の利用で型が確認できます

#for key in val_str:
#    d[key] += 1



for key in val_str:
    #if key not in d:
        # キーが存在しない場合の処理
    #    d[key] = 0
    d[key] += 1


print(list(d.keys()))
print(list(d.values()))

import pandas as pd
import io

#/Users/yogohisashi/yogodev

file_name = '/Users/yogohisashi/yogodev/API_NY_GDP.csv'

#chunksize を指定したとき、返り値は DataFrame ではなく TextFileReader インスタンスとなる。
reader = pd.read_csv(file_name, skiprows=[0, 1], header=5)

#for r in reader:
#    print(type(r), r.shape)


# 先頭から 5行を読み込み
read = reader.get_chunk(5)

print(read)

#for r in read:
#    print(type(r), r.shape)

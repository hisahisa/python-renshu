import csv
import pandas as pd

r = pd.read_csv('/Users/yogohisashi/yogodev/readcsv.txt', chunksize=1, header=None,
                quoting=csv.QUOTE_NONE,doublequote=False,
                #escapechar='¥', encoding='utf-8'
                )
for i in r:
    print( i.iat[0, 0].strip('"') )
    print( i.iat[0, 1].strip('"') )
    #print(str.strip(i))

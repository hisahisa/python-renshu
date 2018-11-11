"""
読み込んだファイルから、特定の条件のみを抽出する
"""
import pandas as pd
from io import StringIO

txt = """col1,col2
1,a
0,b
1,c
0,d"""

df0 = pd.concat(df for df in pd.read_csv(StringIO(txt), chunksize=1))

print(df0)
df1 = pd.concat([df.query('col2 == "a"') for df in pd.read_csv(StringIO(txt), chunksize=1)])

print(df1)

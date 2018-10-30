import pandas as pd
import io

txt = """
id,name,age,state,point
0,Alice,24,NY,64
1,Bob,42, CA,92
2,Charlie,18,CA,70
3,Dave,68,TX,70
4,Ellen,24,CA,88
5,Frank,30,NY,57
6,Bob,42, LA,92
"""

df = pd.read_csv(io.StringIO(txt), index_col="id")
print(df.groupby('state').mean())
print('------')

print(df.groupby('state').agg(
    {'name': lambda x: ','.join(x),
     'age': 'mean',
     'point': 'mean'}))
print('------')
#print(df.duplicated(subset=['name', 'point']))

print(df.groupby(['name']).agg(
    {'state': list,
     'age': 'mean',
     'point': 'mean'}))

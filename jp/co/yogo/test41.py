import pandas as pd
import io

#/Users/yogohisashi/yogodev

file_name = '/Users/yogohisashi/yogodev/API_NY_GDP.csv'
df = pd.read_csv(file_name, skiprows=[0, 1])
print(df.shape)
print('----------')
print(df.head())

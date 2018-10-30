import pandas as pd

# 重複をチェックする

def file_check(filename):
    for chunk in pd.read_csv(filename, delimiter=',',
            iterator=True, parse_dates=[1], encoding='shift-jis',
            usecols=[ 3, 4, 5, 6, 7, 8], names=( 'A', 'B', 'C', 'D', 'E', 'F'), index_col=0):

        return chunk.duplicated().value_counts()[True] # 重複行のカウント
        #return chunk[chunk.duplicated()] # 重複行の抽出


print(file_check('/Users/yogohisashi/yogodev/KEN_ALL.CSV'))
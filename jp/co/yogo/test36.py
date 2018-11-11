"""
大量データを少しずつ読ませたい場合
"""
import pandas as pd


def chunck_generator(filename, header=False, chunk_size=10):
    for chunk in pd.read_csv(filename, delimiter=',',
                             iterator=True, chunksize=chunk_size, parse_dates=[1], encoding='shift-jis',
                             usecols=[ 3, 4, 5, 6, 7, 8], names=( 'A', 'B', 'C', 'D', 'E', 'F'), index_col=0):
        #yield (chunk.loc['i'] % 2 == 0)
        yield (chunk)


def _generator(filename, header=False, chunk_size=10):
    chunk = chunck_generator(filename, header=False, chunk_size=10)
    for row in chunk:
        yield row


if __name__ == "__main__":
    filename = '/Users/yogohisashi/yogodev/KEN_ALL.CSV'
    generator = _generator(filename=filename)
    while True:
        print(next(generator))


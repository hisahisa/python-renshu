"""
大量データを少しずつ読ませたい場合
"""
import pandas as pd


def chunck_generator(filename, chunk_size=10):
    for chunk in pd.read_csv(filename, delimiter=',',
                             iterator=True, chunksize=chunk_size, parse_dates=[1], encoding='shift-jis', header=2):
        # yield (chunk.loc['i'] % 2 == 0)
        yield (chunk)


def _generator(filename):
    chunk = chunck_generator(filename)
    for row in chunk:
        yield row


if __name__ == "__main__":
    filename = '/Users/yogohisashi/yogodev/API_NY_GDP.csv'
    generator = _generator(filename=filename)
    try:
        while True:
            print(next(generator))
    except StopIteration:
        print('stopIte')

    #finally:
    #    del generator

import time
from collections import defaultdict

start_time = time.perf_counter()

file_name = "/Users/yogohisashi/yogodev/item_product.txt"


header_skipped = False
sales = defaultdict(lambda: 0)
with open(file_name, 'r') as f:
    for line in f:
        if not header_skipped:
            header_skipped = True
            continue
        line = line.split(",")
        print(line)
        if len(line) > 1:
            product = line[0]
            num_sales = int(line[1])
            sales[product] += num_sales


top10 = sorted(sales.items(), key=lambda x:x[1], reverse=True)[:10]

print(top10)

print("perf_counter = {:.5f}".format((time.perf_counter() - start_time)))


import pandas as pd
import time

start_time = time.perf_counter()
file_name = "/Users/yogohisashi/yogodev/item_product.txt"

data = pd.read_csv(file_name, names=('Product', 'ItemsSold'))
top10 = data.groupby("Product")["ItemsSold"].sum()[:10]

#print(top10)

print(top10.sort_index( ascending=False))


print("perf_counter = {:.5f}".format((time.perf_counter() - start_time)))
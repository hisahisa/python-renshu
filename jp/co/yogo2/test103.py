import pandas as pd
import time

start_time = time.perf_counter()
file_name = "/Users/yogohisashi/yogodev/item_product.txt"

data = pd.read_csv(file_name, names=('Product', 'ItemsSold'))
top10 = data.groupby("Product")["ItemsSold"].sum()[:10]

#print(top10)

print(top10.sort_index( ascending=False))


print("perf_counter = {:.5f}".format((time.perf_counter() - start_time)))

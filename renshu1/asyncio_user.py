import asyncio
import random
import time
from renshu1.asyncio_tool import request_pro_con


async def a_my_iterator(n):
    for x in range(1, n):
        # produce an item
        # print('producing item{}/{}'.format(x, n-1))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        item = str(x)
        # put the item in the queue
        yield item, n-1


def my_iterator(n):
    for x in range(1, n):
        # # produce an item
        # print('producing item{}/{}'.format(x, n-1))
        # simulate i/o operation using sleep
        time.sleep(random.random())
        item = str(x)
        # put the item in the queue
        yield item, n-1

async def print_async(item, consumer):
    st = time.time()
    print('item {} consumer:{} ...'.format(item, consumer))
    # simulate i/o operation using sleep
    sl = random.random()
    await asyncio.sleep(sl)
    # process the item
    print('item {} consumer:{}...done({:.3f}, {:.3f})'.format(item, consumer, sl, time.time() - st))
    return item

time_sta = time.time()
print("=== Pattern A ===")
asyncio.run(request_pro_con(3, print_async, my_iterator(10+1)))
time_end = time.time()
# 経過時間（秒）
tim = time_end - time_sta
print(tim)

time_sta = time.time()
print()
print("=== Pattern B ===")
asyncio.run(request_pro_con(3, print_async, a_my_iterator(10+1)))
time_end = time.time()
tim = time_end - time_sta
print(tim)

import asyncio
import time


async def worker(i):
    print(f"Worker {i}: セマフォの取得に成功")
    await asyncio.sleep(3)
    print(f"Worker {i}: セマフォを開放")


async def main():
    sem = asyncio.Semaphore(value=3)

    async def async_limited(num):
        async with sem:
            return await worker(num)

    phases = [async_limited(i) for i in range(1, 12)]
    await asyncio.gather(*phases)
    print("main coroutine")

s = time.time()
asyncio.run(main())
print("all worker is done")
print('processing time: {}'.format(time.time()-s))

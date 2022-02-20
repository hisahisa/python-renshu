import asyncio
import time


async def worker(i):
    print(f"Worker {i}: セマフォの取得に成功")
    await asyncio.sleep(3)
    print(f"Worker {i}: セマフォを開放")
    return 'item: {} end'.format(i)


async def main():
    semaphore = asyncio.Semaphore(value=3)

    async def async_limited(num):
        async with semaphore:
            return await worker(num)

    phases = [async_limited(i) for i in range(1, 12)]
    results = []
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print('received answer {!r}'.format(answer))
        results.append(answer)
    print('results: {!r}'.format(results))
    return results
    print("main coroutine")


s = time.time()
asyncio.run(main())
print("all worker is done")
print('processing time: {}'.format(time.time()-s))

import asyncio


async def request_pro_con(num_consumer, async_func, iterator):
    async def consume(async_func, queue, consumer):
        while True:
            # wait for an item from the producer
            print(f'start queue.get consumer: {consumer}')
            item = await async_func(await queue.get(), consumer)
            # Notify the queue that the item has been processed
            print(f'Notify the queue that the item has been processed item: {item}')  # アイテムの使用完了をキューに知らせる
            queue.task_done()

    async def produce(queue, iterator):
        if hasattr(iterator, "__aiter__"):
            async for item, n in iterator:
                # put the item in the queue
                await queue.put(item)
                # produce an item
                print('producing item{}/{}'.format(item, n))
        else:
            for item, n in iterator:
                # put the item in the queue
                await queue.put(item)
                # produce an item
                print('producing item{}/{}'.format(item, n))

        # wait until the consumer has processed all items
        print('wait until the consumer has processed all items')  # キューの全アイテムが消費されるのを待つ
        await queue.join()

    async def watchdog(producer, consumes, timeout=1.0):
        print('start watch dog')
        while not producer.done():
            print('not producer.done')
            await asyncio.sleep(timeout)
            for t in consumes:
                print(f'consume task check. {t.get_name()}')
                if t.done():
                    raise ValueError("consume is done." + str(t))

    queue = asyncio.Queue(5)
    # schedule the consumer
    consumers = [asyncio.create_task(consume(async_func, queue, f'consumer_{i+1}'),
                                     name=f'consumer_{i+1}') for i in range(num_consumer)]
    # schedule the producer
    producer = asyncio.create_task(produce(queue, iterator))

    # run the watchdog and wait for completion
    print('*************** gathering start ***************')
    await asyncio.gather(producer, watchdog(producer, consumers))

    # the consumer is still awaiting for an item, cancel it
    for t in consumers:
        print('{} is cancel'.format(t.get_name()))  # コンシューマーキャンセル
        t.cancel()

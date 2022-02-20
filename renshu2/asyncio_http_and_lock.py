# https://stackoverflow.com/questions/57760869/python-how-to-use-asyncio-with-huge-csv-files-to-send-asynchronous-requests-fro
import asyncio
import aiohttp

import csv

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except Exception as e:
        print(url, str(e))
        return False


async def write_result(result, writer):
    async with asyncio.Lock():   # lock for gracefully write to shared file object
        #res = [<needed parts from result, >] # <- adjust a resulting list of strings
        res = None
        writer.writerow(res)


async def validate_page(session, url, writer):
    res = await fetch(session, url)
    if res:
        await write_result(res, writer)


async def main():
    async with aiohttp.ClientSession() as session:
        with open('urls.csv') as csv_in, open('results.csv', 'a') as csv_out:
            writer = csv.writer(csv_out, delimiter=',')
            aws = [validate_page(session, url.strip(), writer) for url in csv_in]
            await asyncio.gather(*aws)
            print('!--- finished processing')

asyncio.run(main())
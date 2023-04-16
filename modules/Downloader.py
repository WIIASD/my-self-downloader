import tqdm.asyncio as tqdma
import asyncio
import aiohttp
from time import perf_counter

header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    "origin": "https://v.myself-bbs.com",
    "referer": "https://v.myself-bbs.com/"
}

async def fetch(s, url):
    async with s.get(url) as r:
        if r.status != 200:
            r.raise_for_status()
        return await r.read()

async def download(s, url, i):
    try:
        res = await fetch(s, url)
        return res
    except Exception as e:
        print(f"failed to download url with id={i}")
        # TODO properly handle this instead of returning a piece of shit
        return b'shit'

async def fetch_all(s, urls):
    tasks = []
    # TODO make this index prettier
    i = 0 
    for url in urls:
        task = asyncio.create_task(download(s, url, i))
        tasks.append(task)
        i += 1
    res = await tqdma.tqdm_asyncio.gather(*tasks)
    return res

async def _downloadAll(urls):
    async with aiohttp.ClientSession(headers=header) as session:
        results = await fetch_all(session, urls)
        return results

def downloadAll(urls):
    return asyncio.run(_downloadAll(urls))

if __name__ == '__main__':
    urls = [
        "https://myself-bbs.com/thread-48795-1-1.html",
        "https://myself-bbs.com/thread-49165-1-1.html",
        "https://myself-bbs.com/thread-49561-1-1.html",
        "https://myself-bbs.com/thread-49498-1-1.html",
        "https://myself-bbs.com/thread-48795-1-1.html",
        "https://myself-bbs.com/thread-49165-1-1.html",
        "https://myself-bbs.com/thread-49561-1-1.html",
        "https://myself-bbs.com/thread-49498-1-1.html",
    ]
    start = perf_counter()
    results = downloadAll(urls)
    stop = perf_counter()
    print("time taken:", stop - start)
    pass
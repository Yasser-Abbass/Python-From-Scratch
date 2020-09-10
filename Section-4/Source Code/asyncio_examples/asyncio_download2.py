import time
import httpx
import asyncio
from pathlib import Path

photos = [
    'https://unsplash.com/photos/LxaorEDmI3c/download?force=true',
    'https://unsplash.com/photos/4rDCa5hBlCs/download?force=true',
    'https://unsplash.com/photos/jFCViYFYcus/download?force=true',
    'https://unsplash.com/photos/EwKXn5CapA4/download?force=true',
    'https://unsplash.com/photos/1Z2niiBPg5A/download?force=true',
    'https://unsplash.com/photos/G15G-Any-D0/download?force=true',
    'https://unsplash.com/photos/01_igFr7hd4/download?force=true',
    'https://unsplash.com/photos/78A265wPiO4/download?force=true',
    'https://unsplash.com/photos/tGTVxeOr_Rs/download?force=true',
    'https://unsplash.com/photos/hFzIoD0F_i8/download?force=true'
]


async def download(url):
    print(f'Starting to download from {url}')
    client = httpx.AsyncClient()
    try:
        response = await client.get(url)
    finally:
        await client.aclose()

    Path('./photos').mkdir(exist_ok=True)
    fname = response.headers['Content-Disposition'].split('filename=')[-1].replace('"', '')
    fname = './photos/' + fname
    with open(fname, 'wb') as fs:
        fs.write(response.content)


async def main():
    await asyncio.gather(*(download(photo) for photo in photos))

start = time.time()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
stop = time.time() - start
print(f'Total time elapsed is {stop}')
#Total time elapsed is 11.43738055229187
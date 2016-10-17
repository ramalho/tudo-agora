"""Download flags of top 20 countries by population

Asynchronous version

Sample run::

    $ python3 flags_await.py
    BD BR CD CN DE EG ET FR ID IN IR JP MX NG PH PK RU TR US VN
    20 flags downloaded in 10.16s

"""
import os
import time
import sys

import asyncio
import aiohttp

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://localhost:8002/flags/'  # Vaurien proxy: delay

DEST_DIR = 'downloads/'


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


async def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = await aiohttp.request('GET', url)
    image = await resp.read()
    return image


async def download_one(cc):
    image = await get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    task_list = [download_one(cc) for cc in cc_list]
    super_task = asyncio.wait(task_list)
    done, _ = loop.run_until_complete(super_task)
    loop.close()

    return len(done)


def main():
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main()

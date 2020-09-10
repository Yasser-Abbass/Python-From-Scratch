import asyncio
import datetime
import random
import time


def print_now(name, sleep):
    now = datetime.datetime.now()
    print(f"{name} sleeping for {sleep} {now}")


async def print_pn(name=''):
    while True:
        sleep = random.randint(0, 3)
        print_now(name, sleep)
        await asyncio.sleep(sleep)


async def main():
    try:
        await asyncio.wait_for(asyncio.gather(
            print_pn('One'),
            print_pn('Two'),
            print_pn('Three'),
        ), 10)
    except asyncio.TimeoutError:
        print('Your time is up')


asyncio.run(main())


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
    await print_pn('One')
    await print_pn('Two')
    await print_pn('Three')

asyncio.run(main())


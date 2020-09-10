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
        names = ['One', 'Two', 'Three']
        tasks = [print_pn(name) for name in names]
        done, pending = await asyncio.wait(tasks, timeout=10)
        for pend in pending:
            print(f"{pend.get_name()} is about to be canceled")
            pend.cancel()
    except asyncio.TimeoutError:
        print('Your time is up')


asyncio.run(main())


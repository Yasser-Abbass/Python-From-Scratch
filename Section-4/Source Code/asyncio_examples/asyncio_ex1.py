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

asyncio.run(print_pn('Hello'))
#loop = asyncio.get_event_loop()
#loop.run_until_complete(print_pn('Hello'))
#loop.close()
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
    names = ['One', 'Two', 'Three']
    tasks = [asyncio.create_task(print_pn(name)) for name in names]
    for task in tasks:
        print(task.get_name())
    await asyncio.wait(tasks, timeout=5)
    print('Main Task')


asyncio.run(main())


import asyncio
import datetime
import random
import time


def print_now(name, sleep):
    now = datetime.datetime.now()
    print(f"{name} sleeping for {sleep} {now}")


async def print_pn(name=''):
    sleep = random.randint(0, 3)
    print_now(name, sleep)
    await asyncio.sleep(sleep)
    return name


def callback(ft):
    print(f'This is from {ft.result()}')


async def main():
    names = ['One', 'Two', 'Three']
    tasks = [asyncio.create_task(print_pn(name)) for name in names]
    for task in tasks:
        print(task.get_name())
        task.add_done_callback(callback)
    #await asyncio.wait(tasks, timeout=5)
    await asyncio.sleep(5)
    print('Main Task')


asyncio.run(main())


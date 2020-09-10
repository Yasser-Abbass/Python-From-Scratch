import time
import concurrent.futures


def fact(num):
    start = time.time()
    x = 1
    for i in range(1, num):
        x *= i
    time.sleep(1)
    stop = time.time() - start
    print(f'time elapsed {stop}')


if __name__ == '__main__':
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executer:
        for i in range(3):
            executer.submit(fact, 50000)
    stop = time.time() - start
    print(f'Total time elapsed {stop}')
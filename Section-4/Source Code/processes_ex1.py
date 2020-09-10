import time
import multiprocessing


def fact(num):
    start = time.time()
    x = 1
    for i in range(1, num):
        x *= i
    time.sleep(1)
    stop = time.time() - start
    print(f'time elapsed {stop}')


if __name__ == '__main__':
    processes = []
    num_processes = 3
    for i in range(num_processes):
        print(f'registering process {i}')
        p = multiprocessing.Process(target=fact, args=(50000,))
        processes.append(p)
    start = time.time()
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    stop = time.time() - start
    print(f'Total time elapsed {stop}')

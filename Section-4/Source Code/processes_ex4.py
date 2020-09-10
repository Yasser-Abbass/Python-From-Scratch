import multiprocessing


def get_square(mylist, result):

    print(f'Process id {multiprocessing.current_process().name}')
    for val in mylist:
        result.append(val**2)


mylist = [3, 4, 5]

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        result2 = manager.list()
        p1 = multiprocessing.Process(target=get_square, args=(mylist, result2))
        p1.start()
        p1.join()
        print(f'Process id {multiprocessing.current_process().name}')
        print(result2)

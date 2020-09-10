import multiprocessing

# result = []
#
#
# def get_square(mylist):
#     global result
#     print(f'Process id {multiprocessing.current_process().name}')
#     for i in mylist:
#         result.append(i**2)
#     print(f'The result is {result}')
#
# mylist = [3, 4, 5]
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=get_square, args=(mylist,))
#     p1.start()
#     p1.join()
#     print(f'Process id {multiprocessing.current_process().name}')
#     print(result)

result_array = multiprocessing.Array('i', 3)

def get_square(mylist, result):

    print(f'Process id {multiprocessing.current_process().name}')
    for idx, val in enumerate(mylist):
        result[idx] = val**2
    

mylist = [3, 4, 5]

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=get_square, args=(mylist, result_array))
    p1.start()
    p1.join()
    print(f'Process id {multiprocessing.current_process().name}')
    for i in range(3):
        print(result_array[i])
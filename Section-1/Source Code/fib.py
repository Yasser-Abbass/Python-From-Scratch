import sys


def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

args = sys.argv


if len(args) > 1:
    x = int(args[1])
    print(fib(x))
else:
    print('Please enter a number to calculate fib')

#x = fib(100)
#print(x)


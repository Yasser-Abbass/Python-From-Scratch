import sys

def newfib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
     
if __name__=='__main__':
    x = newfib(int(sys.argv[1]))
    print(x)
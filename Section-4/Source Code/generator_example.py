def fact(num):
    result = 1
    for i in range(1, num+1):
        result *= i
        yield result


x = fact(100)
for y in x:
    print(y)

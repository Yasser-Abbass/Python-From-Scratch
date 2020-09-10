import sys


class Fib:
    def __init__(self, num):
        self.num = num
        self.a = 0
        self.b = 1
        self.result = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.num:
            self.result = self.a
            self.a, self.b = self.b, self.b + self.a

            return self.result
        else:
            raise StopIteration


if __name__ == "__main__":
    x = int(sys.argv[1])
    y = Fib(x)
    results = []
    for result in y:
        results.append(result)

    print(results)

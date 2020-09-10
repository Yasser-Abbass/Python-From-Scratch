def dec_fun(fun):
    print("Before executing wrapper")
    def wrapper_fun():
        print('Inside wrapper function')
        return fun()
    print('After executing wrapper')
    return wrapper_fun


@dec_fun
def print_something():
    print('Hello')


print_something()

def test_fun(*args, **kwargs):
    print(args)
    print(kwargs)


test_fun(1, 3, 5, a=1, b=2, c=3)

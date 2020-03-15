def func(*param_func):
    for function in param_func:
        print("{:^20}".format(function()))


func(lambda: 4, lambda: 4 + 6, lambda: 'João')

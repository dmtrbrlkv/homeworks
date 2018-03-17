from functools import wraps
import datetime
from time import sleep


def func_timer(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        begin = datetime.datetime.now()
        x = func(*args, **kwargs)
        end = datetime.datetime.now()
        print("{} seconds passed".format(end - begin))
        return x
    return decorated



class FuncCounter(object):
    def __init__(self):
        self.count = 0

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            self.count += 1
            print("{} вызвана {} раз".format(func.__name__, self.count))
            return func(*args, **kwargs)
        return decorated



# @func_timer
# def deep_copy(l):
#     import copy
#     return copy.deepcopy(l)
#
#
#
# for i in range(100):
#     print(i)
#     deep_copy([x for x in range(1000*i)])

@FuncCounter()
def do_smth(x, y):
    return x + y


@FuncCounter()
def do_smth2(x, y):
    return x + y


for i in range(10):
    do_smth(1, 1)
    do_smth2(1, 1)




def decor_process_logger(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        print("Function {} is started {}".format(func.__name__, datetime.datetime.now()))
        x = func(*args, **kwargs)
        print("Function {} is over {}".format(func.__name__, datetime.datetime.now()))
        return x


    print("decorator for {} is created {}".format(func.__name__, datetime.datetime.now()))
    return decorated


@decor_process_logger
def sleep_func(sec):
    sleep(sec)


for i in range(1, 4):
    sleep_func(i)



def catch_exception(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            x = func(*args, **kwargs)
            return x
        except Exception as e:
            print(e)
    return decorated

@catch_exception
def to_int(i):
    return int(i)

for i in [1, "ad", "2", None]:
    print(to_int(i))
import random


def random_gen(k = 100):
    while True:
        yield random.randint(0, k)


x = random_gen()
print(next(x))
print(next(x))


def range_gen(start, stop, step = 1):
    i = start
    while i < stop:
        yield i
        i += step


x = range_gen(10, 20)
print(list(x))
x = range_gen(1, 100, 20)
print(list(x))


def map_gen(func, lst):
    i = 0
    l = len(lst)
    while i < l:
        yield func(lst[i])
        i += 1


x = map_gen(lambda x: x**2, [1, 2, 3])
print(list(x))
x = map(lambda x: x**2, [1, 2, 3])
print(list(x))


def enum_gen(lst, begin_index = 0):
    i = begin_index
    l = len(lst)
    c = 0
    while c < l:
        yield i, lst[c]
        i += 1
        c += 1

x = enum_gen([1, 2, 3], 5)
print(list(x))
x = enumerate([1, 2, 3], 5)
print(list(x))


def zip_gen(lst1, lst2):
    i1 = 0
    i2 = 0
    l1 = len(lst1)
    l2 = len(lst2)
    while i1 < l1 or i2 < l2:
        item1 = lst1[i1] if i1 < l1 else None
        item2 = lst2[i2] if i2 < l2 else None
        yield item1, item2
        i1 += 1
        i2 += 1


x = zip_gen([1, 2, 3], ["a", "b"])
print(list(x))
x = zip([1, 2], ["a", "b", "c"])
print(list(x))



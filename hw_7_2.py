res = list(map(lambda x: x % 5, [1, 4, 5, 30, 99]))
print(res)


res = list(map(str, [3, 4, 90, -2]))
print(res)

res = list(filter(lambda x: not isinstance(x, str), ['some', 1, 'v', 40, '3a', str]))
print(res)
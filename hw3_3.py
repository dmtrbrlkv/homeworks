def sum_by_sign(x, y):
    if x > 0 and y > 0:
        return x + y
    elif x < 0 and y < 0:
        return x - y
    else:
        return 0


def max_from_3(x, y, z):
    l = sorted([x, y, z])
    print(l[2], l[1])


def get_elements_by_flag(numbers: list, flag: bool) -> list:
    res = []
    for element in numbers:
        if flag:
            if element % 2:
                res.append(element)
        else:
            if not element % 2:
                res.append(element)
    return res


def max_min_by_numbers(*numbers):
    return [max(numbers), min(numbers)]


def register_by_flag(text: str, flag: bool = True) -> str:
    return text.upper() if flag else text.lower()


def glue_strings(*strings, glue = ":"):
    res = ""
    for string in strings:
        if len(string) >= 3:
            if res:
                res = res + glue + string
            else:
                res = string
    return res


# while True:
#     max_from_3(*map(int, input("Введите три числа: ").split()))


print(get_elements_by_flag([1, 2, 3, 4, 5, 6, 7], True))
print(get_elements_by_flag([1, 2, 3, 4, 5, 6, 7], False))

print(max_min_by_numbers(1, 2, 3, 4, 5, 6, 67))

print(register_by_flag("Hello, World!", True))
print(register_by_flag("Hello, World!", False))
print(register_by_flag("Hello, World!"))


print(glue_strings("hellow", ",", "world", ")))", glue = "#"))

import  sys

try:
    raise Exception("qqq")
except:
    print(sys.exc_info())

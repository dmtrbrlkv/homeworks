def firstDuplicate(a):
    res_index = -1
    res = -1
    for index, x in enumerate(a):
        if x in a[index+1:]:
            cur_index = a.index(x, index+1)
            if res_index == -1:
                res_index = cur_index
                res = x
            elif res_index > cur_index:
                res_index = cur_index
                res = x
    return res


print(firstDuplicate([2, 3, 3, 1, 5, 2]))
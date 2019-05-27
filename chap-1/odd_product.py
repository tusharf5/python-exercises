def any_odd_prod(lists):
    exist = False
    num = None
    for d in range(len(lists)):
        if exist:
            break
        for k in range(len(lists)):
            if (lists[d] * lists[k]) % 2 != 0 and d != k:
                num = lists[d], lists[k], lists[d] * lists[k]
                exist = True
                break
    return exist, num


print(any_odd_prod([2, 3, 4, 7]))
print(any_odd_prod([2, 4]))
print(any_odd_prod([2, 4, 6, 8]))
print(any_odd_prod([2, 4, 3, 6, 8, 9]))

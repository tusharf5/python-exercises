import time


def all_distinct(list):
    exist = {}
    allDistinct = True
    for d in range(len(list)):
        if list[d] in exist:
            allDistinct = False
            break
        exist[list[d]] = True
    return allDistinct


def all_distinct_bad(list):
    allDistinct = True
    for d in range(len(list)):
        if allDistinct == False:
            break
        for k in range(len(list)):
            if list[k] == list[d] and k != d:
                allDistinct = False
                break
    return allDistinct


print(all_distinct([1, 2, 3, 4, 5]))
print(all_distinct([1, 2, 3, 4, 5, 1]))
print(all_distinct([1, 2, 3, 4, 5, 10, 9, 9]))
print(all_distinct([1, 2, 3, 4, 5, 6, 7, 8, 9]))

longlist = list(range(10000))
longlist += [9999]

start = time.time()
print(all_distinct(longlist))
end = time.time()
print('All Distinct', end - start)

start = time.time()
print(all_distinct_bad(longlist))
end = time.time()
print('All Bad Distinct', end - start)

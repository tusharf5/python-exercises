simpleList = ['1', '2', '3', '4']

simpleTouple = (1, 2, 3, 4)

simpleSet = {1, 2, 3, 4}

simpleDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
              'e': simpleSet, 'f': {'new': 'world'}}

simpleList += [10000]

print(simpleList)
print(simpleTouple)
print(simpleSet)
print(simpleDict)
print(simpleDict.keys())
print(simpleDict.values())
print(simpleDict.items())


for data in range(5, 20, 5):
    print(data)
print('\n')


for data in simpleDict.keys():
    print(data, end=' ')
print('\n')

for data in list(simpleDict.keys()):
    print(data, end=' ')
print('\n')


def factors(n):
    k = 1
    while k <= n:
        if n % k == 0:
            yield k
        k += 1


print(factors(100))
print('\n')

for d in factors(1000):
    print(d, sep=",", end="")
print('\n')
print('\n')


def rangeNew(max):
    index = 0
    while index < max:
        yield index
        index += 1


for d in rangeNew(10):
    print(d)

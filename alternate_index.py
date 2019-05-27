def alternate_index(index, list):
    length = len(list) - 1
    return -(length - (index - 1))


listing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(listing[0], '------', listing[alternate_index(0, listing)])
print(listing[3], '------', listing[alternate_index(3, listing)])
print(listing[5], '------', listing[alternate_index(5, listing)])
print(listing[7], '------', listing[alternate_index(7, listing)])
print(listing[8], '------', listing[alternate_index(8, listing)])
print(listing[9], '------', listing[alternate_index(9, listing)])


print(list(range(50, 81, 10)))
print(list(range(8, -9, -2)))

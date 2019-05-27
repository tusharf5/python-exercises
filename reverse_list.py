def reverse_list(list):
  length = len(list) - 1
  newlength = []
  for d in range(length, -1, -1):
    newlength += [list[d]]
  return newlength

print(reverse_list([1,2,3,4,5,6]))
print(reverse_list(['a', 'b', 'c', 'd']))

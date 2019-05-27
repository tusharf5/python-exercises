def minmax(data):
   min = data[0]
   max = data[0]
   for d in data:
     if d < min:
       min = d
     elif d > max:
       max = d
   return min, max

print(minmax((1,2,3,4,5,6,7,8,9)))    
print(minmax((100,99,4,5,6,7,8,9,0)))    
print(minmax((85,98,32,88,23,199)))    

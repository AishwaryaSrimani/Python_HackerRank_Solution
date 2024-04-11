# Q. You are given a 2-D array of size NXM.
    # Your task is to find:
    # 1) The mean along axis 1 
    # 2) The var along axis 0
    # 3) The std along axis None

import numpy

n, m = map(int, input().split())

arr = []
for i in range(n):
    list1 = list(map(int, input().split()))
    arr.append(list1)
    
arr2 = numpy.array(arr)

print(numpy.mean(arr2, axis=1))
print(numpy.var(arr2, axis=0))
print(round(numpy.std(arr2), 11))
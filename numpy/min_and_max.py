# Q. You are given a 2-D array with dimensions NXM.
    # Your task is to perform the min function over axis 1 and then find the max of that.
    # Input Format
    # The first line of input contains the space separated values of N and M.
    # The next N lines contains M space separated integers.
    
import numpy

n, m = map(int, input().split())

arr = []
for i in range(n):
    list1 = list(map(int, input().split()))
    arr.append(list1)
    
arr2 = numpy.array(arr)

x = numpy.min(arr2, axis=1)
y = numpy.max(x)

print(y)

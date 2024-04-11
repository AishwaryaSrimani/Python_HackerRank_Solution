# Q. You are given a 2-D array with dimensions NXM.
    # Your task is to perform the sum tool over axis 0 and then find the product of that result.
    
import numpy

n, m = map(int, input().split())

arr = []
for i in range (n):
    list1 = list(map(int, input().split()))
    arr.append(list1)
    
arr2 = numpy.array(arr)
new_arr = numpy.sum(arr2, axis=0)

print(numpy.prod(new_arr, axis=None))   
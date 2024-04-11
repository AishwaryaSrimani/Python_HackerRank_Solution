# Q. You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

import numpy

arr = list(map(int, input().split()))
arr2 = numpy.array(arr)
print(numpy.reshape(arr2, (3, 3)))
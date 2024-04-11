# Q. You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

import numpy as np

arr_shape = np.array(input().split(sep=' '), dtype='int')

def zeros(shape):
    return np.zeros((shape), dtype='int')

def ones(shape):
    return np.ones((shape), dtype='int')

print(zeros(arr_shape))
print(ones(arr_shape))



# Another way [but this can raise runtime error when working with large data]
m, n, p = list(map(int, input().split(' ')))

print(np.zeros((m, n, p), dtype='i'))
print(np.ones((m, n, p), dtype='i'))

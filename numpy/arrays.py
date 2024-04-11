# Q. You are given a space separated list of numbers.
    # Your task is to print a reversed NumPy array with the element type float.
    
import numpy

def arrays(arr):
    z = list(map(float, arr))
    x = numpy.array(z)
    y = x [::-1]

    return y

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

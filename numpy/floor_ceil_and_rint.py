# Q. You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.

import numpy as np
np.set_printoptions(legacy=1.13)

A = list(map(float, input().split()))
x = np.array(A)

print(np.floor(x), np.ceil(x), np.rint(x), sep='\n')



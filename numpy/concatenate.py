# Q. You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.
    # Input Format
    # The first line contains space separated integers N, M and P.
    # The next N lines contains the space separated elements of the P columns.
    # After that, the next M lines contains the space separated elements of the P columns.

import numpy as np

x = list(map(int, input().split(' ')))

arr1 = []
for i in range (x[0]):
    list1 = list(map(int, input().split(' ')))
    arr1.append(list1)
    arr = np.array(arr1)

arr2 = []
for item in range (x[1]):
    list2 = list(map(int, input().split(' ')))
    arr2.append(list2)
    arr_2nd = np.array(arr2)

print (np.concatenate((arr, arr_2nd), axis=0))

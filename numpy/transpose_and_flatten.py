# Q. You are given a N X M integer array matrix with space separated elements (N = rows and M = columns).
    # Your task is to print the transpose and flatten results.
    
import numpy as np

n, m = (map(int, input().split()))

my_arr = []
for i in range (n):
    list1 = list(map(int, input().split()))
    my_arr.append(list1)
    
new_arr = np.array(my_arr)

print(np.transpose(new_arr))
print(new_arr.flatten())
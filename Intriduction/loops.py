# Q. The provided code stub reads and integer, n, from STDIN. For the list of non-negative integers that are less than n (i<n), print the square of each number on a separate line.

n = int(input())
for i in range(n):
    print(i**2)

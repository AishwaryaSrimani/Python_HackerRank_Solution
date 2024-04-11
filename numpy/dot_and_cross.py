# Q. You are given two arrays A and B. Both have dimensions of NXN.
    # Your task is to compute their matrix product.
    # Input Format
    # The first line contains the integer N.
    # The next N lines contains  space separated integers of array A.
    # The following N lines contains N space separated integers of array B.
    
import numpy

n = int(input())

a = []
for i in range(n):
    ls1 = list(map(int, input().split()))
    a.append(ls1)
A = numpy.array(a)
    
b = []
for item in range(n):
    ls2 = list(map(int, input().split()))
    b.append(ls2)
B = numpy.array(b)

print(numpy.dot(A, B))

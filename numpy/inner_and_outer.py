# Q. You are given two arrays: A and B.
    # Your task is to compute their inner and outer product.
    
import numpy

a = list(map(int, input().split()))
b = list(map(int, input().split()))
A, B = numpy.array(a), numpy.array(b)

print(numpy.inner(A, B))
print(numpy.outer(A, B))
# Q. You are given a two lists A and B. Your task is to compute their cartesian product AXB.
    # Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.
    
from itertools import product

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

print (*list(product(a, b)))

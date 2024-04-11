# Q. You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume -based indexing) with a uniform probability from the list.
    # Find the probability that at least one of the K indices selected will contain the letter: 'a'.
    
from itertools import combinations

N = int(input())
s = input().split()
k = int(input())

x = (list(combinations(s, k)))

b = []
for i in x:
    if 'a' not in i:
        b.append(i)
 
print(1-len(b)/len(x))
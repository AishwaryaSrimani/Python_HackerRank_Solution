# Q. You are given a string S.
    # Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
    # Input Format
    # A single line containing the string S and integer value k separated by a space.
    
from itertools import combinations

s, n = input().split(' ')
num = int(n)
word = sorted(s.upper())

res = []
for i in range(1, num+1):
    res.extend(list(combinations(word, i)))

for i in res:
    print("".join(i))
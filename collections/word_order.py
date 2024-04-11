# Q. You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.

from collections import Counter

n = int(input())

x = []
for i in range(n):
    x.append(input())
    
y = Counter(x)

print(len(y.keys()))
print(*y.values())
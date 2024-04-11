# Q. In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(1, n+1):
    d[input()].append(i)
    
for j in range(0, m):
    v = input()
    if v in d.keys():
        print(*d[v])
    else:
        print(-1)
        
        

# Another way

from collections import defaultdict

n, m = map(int, input().split())
a = defaultdict(list)

for i in range(1, n+1):
    a[input()].append(i)
    
for _ in range(m):
    print(*a.get(input()) or [-1])
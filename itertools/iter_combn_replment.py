# Q. You are given a string S.
    # Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

from itertools import combinations_with_replacement

a = input().split(' ')
y = int(a[1])
s = list(a[0])
w = sorted(s)

li = []
for i in w:
    li.append(i)
    
x=list(combinations_with_replacement(li, y))
e= sorted(x)

for z in e:
    print (''.join(z))
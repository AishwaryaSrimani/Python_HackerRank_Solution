# Q. You are given a string S.
    # Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
    # Input Format
    # A single line containing the space separated string S and the integer value k.
    
from itertools import permutations
a = input().split(' ')
y = int(a[1])

list1 = []
for i in a[0]:
    list1.append(i)
    
x=list(permutations(list1, y))
e=sorted(x)

for item in e:
    print (''.join(item))
# Q. Perform append, pop, popleft and appendleft methods on an empty deque d.

    # Input Format

    # The first line contains an integer N, the number of operations.
    # The next N lines contains the space separated names of methods and their values.
    
from collections import deque

n = int(input())

d = deque()

for i in range(n): 
    x = list(input().split()) 
    if x[0] == 'append': 
        d.append(int(x[1]))
    elif x[0] == 'appendleft':
        d.appendleft(int(x[1]))
    elif x[0] == 'pop':
        d.pop()
    elif x[0] == 'popleft':
        d.popleft()
        
print(*d)
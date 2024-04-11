# Q. You are given a set A and n other sets.
    # Your job is to find whether set A is a strict superset of each of the N sets.
    # Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
    # A strict superset has at least one element that does not exist in its subset.
    
a = set(map(int, input().split()))
n = int(input())

for i in range(n):
    b = set(map(int, input().split()))
    
    if (a.issuperset(b)):
        flag = True
    else:
        flag = False
        break
         
print(flag)
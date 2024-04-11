# Q. You are given two sets, A and B.
    # Your job is to find whether set A is a subset of set B.
    # If set A is subset of set B, print True.
    # If set A is not a subset of set B, print False.
        
a = int(input())
for item in range(0, a):
    b = int(input())
    s1=set(map(int, input().split(' ')))
    c = int(input())
    s2=set(map(int, input().split(' ')))
    result = s1.issubset(s2)
    print (result)   
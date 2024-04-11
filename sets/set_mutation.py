# Q. You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
    # Your task is to execute those operations and print the sum of elements from set A.
    # Input Format
    # The first line contains the number of elements in set A.
    # The second line contains the space separated list of elements in set A.
    # The third line contains integer N, the number of other sets.
    # The next 2*N lines are divided into N parts containing two lines each.
    # The first line of each part contains the space separated entries of the operation name and the length of the other set.
    # The second line of each part contains space separated list of elements in the other set.
    
_ = int(input()) 
setA= set(map(int, input().split())) 
for item in range(int(input())): 
    st = input().split()[0] 
    setB = set(map(int, input().split())) 
    if 'intersection_update' == st: 
        setA.intersection_update(setB) 
    elif 'update' == st: 
        setA.update(setB) 
    elif 'symmetric_difference_update' == st: 
        setA.symmetric_difference_update(setB) 
    elif 'difference_update' == st: 
        setA.difference_update(setB)

print(sum(setA))


# Q. Consider a list (list = []). You can perform the following commands:
    # a. insert i e: Insert integer  at position .
    # b. print: Print the list.
    # c. remove e: Delete the first occurrence of integer .
    # d. append e: Insert integer  at the end of the list.
    # e. sort: Sort the list.
    # f. pop: Pop the last element from the list.
    # r. reverse: Reverse the list.
    # Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
    
arr = []
for i in range(int(input())):
    s = input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])
        
    if s[0] == "append":
        arr.append(s[1])
    elif s[0] == "extend":    
        arr.extend(s[1:])
    elif s[0] == "insert":
        arr.insert(s[1],s[2])
    elif s[0] == "remove":
        arr.remove(s[1])
    elif s[0] == "pop":
        arr.pop()
    elif s[0] == "index":
        print(arr.index(s[1]))
    elif s[0] == "count":
        print(arr.count(s[1]))
    elif s[0] == "sort":
        arr.sort()
    elif s[0] == "reverse":
        arr.reverse()
    elif s[0] == "print":
        print(arr)


# Q. You have a non-empty set , and you have to execute N commands given in N lines.
    # The commands will be pop, remove and discard.
    # Input Format
    # The first line contains integer n, the number of elements in the set .
    # The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
    # The third line contains integer N, the number of commands.
    # The next N lines contains either pop, remove and/or discard commands followed by their associated value.
    
n = int(input())
s = set(map(int, input().split()))
my_set1 = []
for item in range (0, int(input())):
    my_set1.append(input().split(' '))
for commands in my_set1:
    if commands [0] == 'remove':
        s.remove(int(commands[1]))
    elif commands[0] == 'discard':
        s.discard(int(commands[1]))
    elif commands [0] == 'pop':
        s.pop()
print (sum(s))



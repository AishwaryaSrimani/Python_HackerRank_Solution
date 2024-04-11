# Q. Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
    # Input Format
    # The first line of input contains an integer, M.
    # The second line contains M space-separated integers.
    # The third line contains an integer, N.
    # The fourth line contains N space-separated integers.
    
m = int(input())
set1 = set(map(int, input().split()))
n = int(input())
set2 = set(map(int, input().split()))

sort_list = sorted(list(set1^set2))
for i in sort_list:
    print(i)




# Another Way

def solve (set1, set2):
    x = set1-set2
    y = set2-set1
    result = x.union(y)
    sort_r = sorted(result)
    return sort_r
    
def convert(n):
    numbers = [int(num) for num in n.split(' ')]
    number_set = set(numbers)
    return number_set

e = int(input())
m = convert(input())
f = int(input())
n = convert(input())
data = solve(m, n)
for i in data:
    print(i)


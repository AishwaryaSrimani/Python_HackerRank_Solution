# Q. You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
    # Input Format
    # The first line contains an integer N. N is the total number of integers in the list.
    # The second line contains the space separated list of N integers.
    
n=int(input())
nums=list(map(int,input().split()))

print(all(x>0 for x in nums) and any(str(x)==str(x)[::-1] for x in nums))

# Another way

n = int(input())
list_num = list(map(int, input().split()))

is_positive = all(float(num)>=0 for num in list_num)
palindromic = any(num == num[::-1] for num in list_num)

if list_num == is_positive and palindromic:
    print(True)
else:
    print(False)

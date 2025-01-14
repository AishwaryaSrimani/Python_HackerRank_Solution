# Q. Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

n = int(input())
arr = map(int, input().split())
    
x = set(arr)
x.remove(max(x))
print(max(x))

# Another way

x = set(arr)
y = list(x)
y.sort(reverse=True)
print(y[1])

# Q. The included code stub will read an integer, n, from STDIN.
    # Without using any string methods, try to print the following: 123...n (Note: "..." represents the consecutive values in between.)

n = int(input())

for i in range(1, n+1):
        print(i, end="")



# Another way by creating function
def func(n):
    data=""
    for i in range(1, n+1):
        data += str(i)
    return (data)

print(func(n))
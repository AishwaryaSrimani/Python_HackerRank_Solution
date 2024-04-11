# Q. Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
    # Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
    # The design should have 'WELCOME' written in the center.
    # The design pattern should only use |, . and - characters.
    
    
n, m = list(map(int, input().split()))

# Upper part design
size = n//2
for i in range(0, size):
    s= '.|.'*(i+1+i)
    print(s.center(m, "-"))
    
# Center part design
print('WELCOME'.center(m, '-'))

# Lower part design
for j in reversed(range(0, size)):
    x = '.|.'*(j+1+j)
    print(x.center(m, '-'))
# Q. You are given a polynomial p of a single indeterminate (or variable), x.
    # You are also given the values of x and k. Your task is to verify if p(x)==k.
    # Constraints
    # All coefficients of polynomial p are integers.
    # x and k are also integers.
    # Input Format
    # The first line contains the space separated values of x and k.
    # The second line contains the polynomial p.
    
x, k = list(map(int, input().split()))
p = input()

if eval(p) == k:
    print(True)
else:
    print(False)
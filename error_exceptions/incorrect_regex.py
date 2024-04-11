# Q. You are given a string S.
    # Your task is to find out whether S is a valid regex or not.
    # Input Format
    # The first line contains integer T, the number of test cases.
    # The next T lines contains the string S.

import re

t = int(input())

for _ in range(t):
    regex = input()
    
    if any(op + '+' in regex for op in ['*', '+', '?']):
        print("False")
    else:
        try:
            re.compile(regex)
            print("True")
        except re.error:
            print("False")

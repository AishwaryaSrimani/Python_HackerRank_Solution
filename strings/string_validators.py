# Q. You are given a string s. Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
    # In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
    # In the second line, print True if s has any alphabetical characters. Otherwise, print False.
    # In the third line, print True if s has any digits. Otherwise, print False.
    # In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
    # In the fifth line, print True if s has any uppercase characters. Otherwise, print False.

s = input()

alpha_num = sum(c.isalnum() for c in s)
if alpha_num >= 1:
    print (True)
else:
    print (False)
    
alpha = sum(c.isalpha() for c in s)
if alpha >= 1:
    print (True)
else:
    print (False)
    
digit = sum(c.isdigit() for c in s)
if digit >= 1:
    print (True)
else:
    print (False)
    
lower_case = sum(c.islower() for c in s)
if lower_case >= 1:
    print (True)
else:
    print (False)
    
upper_case = sum(c.isupper() for c in s)
if upper_case >= 1:
    print (True)
else:
    print (False)

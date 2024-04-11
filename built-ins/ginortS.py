# Q. You are given a string S.
    # S contains alphanumeric characters only.
    # Your task is to sort the string S in the following manner:
    # All sorted lowercase letters are ahead of uppercase letters.
    # All sorted uppercase letters are ahead of digits.
    # All sorted odd digits are ahead of sorted even digits.
    
string = input()
l, u, o, e = '', '', '', ''

for i in string:
    if i.islower():
        l += i
    elif i.isupper():
        u += i
    elif int(i)%2==0:
        e += i
    elif int(i)%2!=0:
        o += i
print("".join(sorted(l) + sorted(u) + sorted(o) + sorted(e)))

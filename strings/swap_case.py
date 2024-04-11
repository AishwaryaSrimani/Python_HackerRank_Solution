# Q. You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    data = ''
    for i in s:
        if i.islower():
            data += i.upper()
        else:
            data += i.lower()
    return data

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
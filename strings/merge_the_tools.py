# Q. A string, s, of length n where s = c0c1...cn-1.
    # An integer, k, where k is a factor of n.
    # We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string vi such that:
    # The characters in vi are a subsequence of the characters in ti.
    # Any repeat occurrence of a character is removed from the string such that each character in vi occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string vi.
    
def merge_the_tools(string, k):
    # your code goes here
    sb = ''
    for idx, s in enumerate(string, start=1):
        if s not in sb:
            sb += s
        if idx % k == 0:
            print(sb)
            sb=""
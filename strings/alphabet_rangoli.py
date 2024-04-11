# Q. You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
    # The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).
    
def print_rangoli(size):
    # your code goes here
    for i in reversed(range(1, size+1)):
        s = chr(i+96)
        for j in range(i+1, size+1):
            s = f"{chr(j+96)}-{s}-{chr(j+96)}"
        print(s.center((size*4)-3, '-'))
    for i in range(2, size+1):
        s = chr(i+96)
        for j in range(i+1, size+1):
            s = f"{chr(j+96)}-{s}-{chr(j+96)}"
        print(s.center((size*4)-3, '-'))
# Q. A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
    # Print the three most common characters along with their occurrence count.
    # Sort in descending order of occurrence count.
    # If the occurrence count is the same, sort the characters in alphabetical order.
    
from collections import Counter

if __name__ == '__main__':
    s = input()


counts = Counter(sorted(s))

for char, count in counts.most_common(3):
    print(f'{char} {count}')
    
    
    
    
# Another way [But this may raise runtime error]

counts = Counter(sorted(s))

for k, v in counts.most_common(3):
    print(k, v, sep=' ')
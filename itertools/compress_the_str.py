# Q. You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

from itertools import groupby

data = input()
data = [i for i in data]

grouped_data = [(key, list(group)) for key, group in groupby(data)]
grouped = [(len(group), int(key)) for key, group in grouped_data]

print(*grouped)

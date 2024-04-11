# Q. Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
    # Find the total number of distinct country stamps.
    
my_set = []
for item in range(0, int(input())):
    my_set.append(str(input()))
a = my_set
print (len(set(a)))
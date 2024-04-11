# Q. There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i element of A, you add 1 to your happiness. If i element of B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

a =input()
set_a=list(map(int, input().split(' ')))
set_b=set(map(int, input().split(' ')))
set_c=set(map(int, input().split(' ')))

happiness = 0
for x in set_a:
    if x in set_b:
        happiness += 1
    elif x in set_c:
        happiness -= 1
print (happiness)

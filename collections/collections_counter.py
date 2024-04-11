# Q. Raghu is a shoe shop owner. His shop has X number of shoes.
    # He has a list containing the size of each shoe he has in his shop.
    # There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size.
    # Your task is to compute how much money Raghu earned.

    # Input Format

    # The first line contains X, the number of shoes.
    # The second line contains the space separated list of all the shoe sizes in the shop.
    # The third line contains N, the number of customers.
    # The next N lines contain the space separated values of the shoe size desired by the customer and x, the price of the shoe.
    
from collections import Counter

shoes = int(input())
list_s = list(map(int, input().split()))

customers = int(input())
counts = Counter(list_s)

s = 0
for i in range(customers):
    size, price = list(map(int, input().split()))
    if size in counts.keys() and counts[size] > 0:
        s += price
        counts[size] -= 1
        
print(s)
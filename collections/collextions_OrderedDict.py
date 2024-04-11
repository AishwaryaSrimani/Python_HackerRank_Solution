# Q. You are the manager of a supermarket.
    # You have a list of N items together with their prices that consumers bought on a particular day.
    # Your task is to print each item_name and net_price in order of its first occurrence.
    # item_name = Name of the item.
    # net_price = Quantity of the item sold multiplied by the price of each item.
    
from collections import OrderedDict

n = int(input())
od = OrderedDict()

for i in range(n):
    item, price = input().rsplit(maxsplit=1)
    if item in od:
        od[item] = od[item] + int(price)
    else:
        od[item] = int(price)
    
for k, v in od.items():
    print(k, v, sep=' ')
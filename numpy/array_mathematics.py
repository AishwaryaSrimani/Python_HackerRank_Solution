# Q. You are given two integer arrays, A and B of dimensions NXM.
    # Your task is to perform the following operations:
    # 1) Add (A + B)
    # 2) Subtract (A - B)
    # 3) Multiply (A * B)
    # 4) Integer Division (A / B)
    # 5) Mod (A % B)
    # 6) Power (A ** B)

import numpy as np

n, m = map(int, input().split())

a,b=[],[]
for _ in range(n):
    r=list(map(int, input().split()))
    a.append(r)
    
for _ in range(n):
    r=list(map(int, input().split()))
    b.append(r)
A,B=np.array(a),np.array(b) 
  
print(A+B, A-B, A*B, A//B, A%B, A**B, sep='\n')




# Another way [but this can raise runtime error when working with large data]
import numpy as np
x, y = map(int, input().split())
arr_a = np.array(list(map(int, input().split())))
arr_b = np.array(list(map(int, input().split())))

print((arr_a + arr_b).reshape(x,y))
print((arr_a - arr_b).reshape(x,y))
print((arr_a * arr_b).reshape(x,y))
print((arr_a // arr_b).reshape(x,y))
print((arr_a % arr_b).reshape(x,y))
print((arr_a ** arr_b).reshape(x,y))



# Q. You are given two values a and b.
    # Perform integer division and print a/b.
    # In the case of ZeroDivisionError or ValueError, print the error code.
    
a=int(input()) 
for i in range(a): 
    try: 
        b=input().split(" ") 
        print(int(int(b[0])/int(b[1]))) 
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e: 
        print("Error Code:",e)
        
        
    
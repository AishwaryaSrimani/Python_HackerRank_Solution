# Q. Given an integer, n, print the following values for each integer i from 1 to :
    # Decimal
    # Octal
    # Hexadecimal (capitalized)
    # Binary
    # The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.    
    
def print_formatted(number):
    # your code goes here
    spacing = len(format(number, 'b'))
    for i in range(1, number+1):
        print(f"{i:>{spacing}} {oct(i)[2:]:>{spacing}} {hex(i)[2:].upper():>{spacing}} {bin(i)[2:]:>{spacing}}")

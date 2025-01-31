# Q. Given a list of rational numbers,find their product.
    # complete the function line with a reduce statement

from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)      # This is the answer
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
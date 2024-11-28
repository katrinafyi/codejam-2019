#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prime_string' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def primeFactors(n): 
    f = []
        
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        f.append(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            f.append(i)
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        f.append(n)
    return f

def prime_string(n):
    # YOUR SOLUTION HERE
    from collections import defaultdict

    zeroes = defaultdict(lambda: 0)
    strings = primeFactors(n)
    for f in strings:
        zeroes[f] += 1
    s = [(f'{f}' if n == 1 else f'{f}^{n}') for f, n in zeroes.items()]
    return '*'.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    y = prime_string(N)

    fptr.write(y + '\n')

    fptr.close()

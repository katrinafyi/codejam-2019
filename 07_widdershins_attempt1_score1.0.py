#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'widdershins' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
#

letters = ['A', 'B', 'D', 'C']

def letter(l):
    return letters[l%4]

def square_spiral(n, first, x, y):
    d = {}
    
    for i in range(n-1):
        d[0, i] = letter(first)
        d[i, n-1] = letter(first+1)
        d[n-1, i+1] = letter(first+2)
        d[i+1, 0] = letter(first+3)
    return {(x+k[0], y+k[1]): v for k, v in d.items()}
        

def widdershins(n):
    from collections import defaultdict 
    d = defaultdict(lambda: ' ')
    
    for i in range(int(n/2)):
        d.update(square_spiral(n-2*i, -i, i, i))
    
    if n % 2 == 1:
        d[int(n/2), int(n/2)] = 'Z'
    
    s = ''
    for r in range(n):
        for c in range(n):
            s += (d[r,c])
        s += '\n'
    return s
    # YOUR SOLUTION HERE

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    y = widdershins(x)

    fptr.write(y)
    fptr.write('\n')

    fptr.close()

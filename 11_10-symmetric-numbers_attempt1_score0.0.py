#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#

# Complete the 'nth_10_sym' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER nth as parameter.
#
import string
digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

pairs = [(i+1, 9-i) for i in range(9)]

def number_of_n_length(n):
    if n == 1:
        return 1 
    return 9**int(n/2)

def nth_10_sym(nth):
    if nth == 1:
        return '5'
    digits = 0
    seen = 0
    while seen < nth:
        digits += 1
        seen += number_of_n_length(digits)
    
    digits_remaining = digits 
    while digits_remaining > 1:
        
        digits_remaining -= 2
    left = int2base(nth-(seen-number_of_n_length(digits)), 9)
    right = [10-int(x) for x in reversed(left)]
    if digits_remaining == 1:
        return ''.join(left) + '5' + ''.join(map(str, right))
    return ''.join(left) + ''.join(map(str, right))
    print(left, right)
    print(seen, digits)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    for k_itr in range(k):
        n = int(input().strip())

        result = nth_10_sym(n)

        fptr.write(str(result) + '\n')

    fptr.close()

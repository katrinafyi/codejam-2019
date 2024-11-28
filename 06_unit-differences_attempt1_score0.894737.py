#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'differences' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER_ARRAY a as parameter.
#

def reduce_seq(seq):
    out = []
    for i, n in enumerate(seq):
        if i < len(seq)-1:
            out.append(seq[i+1]-n)
    return out
def differences(a):
    original = a
    i = 0
    while True:
        i += 1
        a = reduce_seq(a)
        if len(a) == 1:
            return '{'+str(a[0])+'}'
        if all(x == 0 for x in a):
            return str(i) + ' iterations'
    
    print(reduce_seq(a))
    # YOUR SOLUTION HERE

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x_count = int(input().strip())

    x = list(map(int, input().rstrip().split()))

    y = differences(x)

    fptr.write(y + '\n')

    fptr.close()

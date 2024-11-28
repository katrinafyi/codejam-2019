#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'collatz' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def c(prev):
    if prev % 2 == 0:
        return prev/2
    return 3*prev+1

def collatz(n):
    x = n
    i = 0
    while x != 1:
        i+=1
        x = c(x)
    return i
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    y = collatz(x)

    fptr.write(str(y) + '\n')

    fptr.close()

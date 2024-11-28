#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations

#
# Complete the 'twoSum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER target
#

def twoSum(values, target):
    l = ((a, b) for a, b in combinations(values, 2))
    for pair in l:
        if sum(pair) == target:
            x = pair 
            break 
    if x[1] < x[0]:
        return x[1], x[0]
    return x
    
        
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x_count = int(input().strip())

    x = list(map(int, input().rstrip().split()))

    n = int(input().strip())

    y = twoSum(x, n)

    fptr.write(' '.join(map(str, y)))
    fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'optimalAverages' function below.
#
# The function is expected to return a FLOAT.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def reduce_avg(arr):
    print(arr)
    if len(arr) == 1:
        return arr[0]
    out = []
    running_max = 0
    for i in range(len(arr)-1):
        this_avg = reduce_avg(arr[:i] +[(arr[i]+arr[i+1])/2]+ arr[i+2:])
        if this_avg > running_max:
            running_max = this_avg
    return running_max

def optimalAverages(arr):
    return (reduce_avg(arr))
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = optimalAverages(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divide_cash' function below.
#
# The function accepts 2D_INTEGER_ARRAY d12 as parameter.
#

def divide_cash(d12):
    #
    # The input is a list of pairs [list of length 2]
    # Print "True" or "False"
    #
    s = 0 
    for value, n in d12:
        s += value*n 
    print( 0 == s % 2)

if __name__ == '__main__':
    n = int(input().strip())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    divide_cash(a)

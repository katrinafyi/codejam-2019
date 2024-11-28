#!/bin/python3

import math
import os
import random
import re
import sys
import math


def bit_transpose(n):
    n = bin(n)[2:].rjust(16, '0')
    
    length = 4#math.ceil(len(n)**(0.5))
    
    s = ''
    dim= length
    for shift in range(dim):
        for offset in range(dim):
            try:
                x = n[shift+offset*dim]
            except IndexError:
                x = '0'
            s += x
    return int(s, 2)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    y = bit_transpose(x)

    fptr.write(str(y) + '\n')

    fptr.close()

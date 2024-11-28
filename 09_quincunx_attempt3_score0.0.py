#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quincunx' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER rad
#  2. STRING lines
#



def nw(rad):
    return [(rad-1-i, 1+i) for i in range(rad-1)]

def sw(rad):
    return [((rad-1-i)+rad, 2*rad-(1+i)-rad) for i in range(rad-1)]

def se(rad):
    return [(rad-1-i+rad, 1+i+rad) for i in range(rad-1)]

def ne(rad):
    return [((rad-1-i), 2*rad-(1+i)) for i in range(rad-1)]

def cn(rad):
    return [(1+i, rad) for i in range(rad-1)]

def cs(rad):
    return [(1+i+rad, rad) for i in range(rad-1)]

def cw(rad):
    return [(rad, 1+i) for i in range(rad-1)]

def ce(rad):
    return [(rad, 1+i+rad) for i in range(rad-1)]

chars = {
    'nw': '/',
    'sw': '\\',
    'se': '/',
    'ne': '\\',
    'cn': '|',
    'cs': '|',
    'ce': '-',
    'cw': '-'
}

def quincunx(rad, lines):
    # YOUR SOLUTION HERE
    from collections import defaultdict 
    d = defaultdict(lambda: '.')
    d[0, rad] = '#'
    d[rad, 0] = '#'
    d[rad, rad] = '#'
    d[rad, 2*(rad)] = '#'
    d[2*(rad), rad] = '#'
    
    for segment in lines.split(','):
        if segment not in globals():
            segment = segment[::-1]
        #print(segment)
        for pos in (globals()[segment])(rad):
            d[pos] = chars[segment]
       
    s = ''
    
    for row in range(2*rad+1):
        for col in range(2*rad+1):
            s += (d[row,col])
        s += '\n'
    return s    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    r = int(input().strip())

    try:
      s = input()
    except:
      s = ""

    y = quincunx(r, s)

    fptr.write('\n'.join(y))
    fptr.write('\n')

    fptr.close()

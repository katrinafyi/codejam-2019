#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import cycle

#
# Complete the 'decypher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING cypher
#  2. STRING key
#

def decypher(cypher, key):
    s = ''
    iterable = cycle(key)
    for c in cypher:
        
        is_upper = ord('A')<=ord(c)<=ord('Z')
        if not (is_upper or ord('a')<=ord(c)<=ord('z')):
            s += c
            continue
            
        k = next(iterable)
        x= chr((ord(c.lower())-(ord(k)-ord('A')) -ord('a'))%26 + ord('a'))
        if is_upper:
            x = x.upper()
        s += x
    return s
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = input()

    k = input()

    y = decypher(c, k)

    fptr.write(y + '\n')

    fptr.close()

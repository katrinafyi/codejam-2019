#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import product

def get_elem(matrix, indexes):
    """
    Given indexes = [a, b, c, ...], returns 
    matrix[a][b][c][...].
    """
    obj = matrix
    for ind in indexes:
        obj = obj[ind]
    return obj

def make_tupledict(matrix, *names):
    """Converts a matrix (in list of lists form) to a dictionary with tuples
    as keys.
    
    Arguments:
        matrix {List[List[...]]} -- matrix as list of lists (row-major order).
        names {List[List[Any]]} -- row/column names, in the order they are 
        in the list format.
    
    Returns:
        Dict[Tuple[...], int|float] -- dictionary indexed by name tuples.
    """
    d = {}
    ranges = [range(len(x)) for x in names]
    for r in product(*ranges):
        key = tuple(name[i] for name, i in zip(names, r))
        d[key] = get_elem(matrix, r)
    return d

#
# Complete the 'kingdomino' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY tiles as parameter.
#

shifts = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

from collections import deque

def bfs(start_position):
    to_check = deque()
    to_check.append(start_position)
    cx, cy = start_position
    letter = tiles[start_position].lower()
    print()
    print('starting', letter)
    score = 0
    while to_check:
        try:
            cx, cy = to_check.pop()
            available.remove((cx, cy))
            print('checking', cx, cy)
            x,y = cx, cy
            score += 1
            if tiles[x,y].isupper():
                score += 1
            for xs, ys in shifts:
                nx, ny = x + xs, y + ys
                if (nx, ny) in available and tiles[nx, ny].lower() == letter :
                    to_check.append((nx, ny))   
        except Exception:
            continue
    return score**2

def kingdomino(t):
    global tiles, available
    length = len(t)
    # YOUR SOLUTION HERE
    tiles = (make_tupledict(t, list(range(length)), list(range(length)) ))
    
    
    available = set(tiles.keys())
    print(tiles)
    s = 0
    while available:
        a = next(iter(available))
        # print(a)
        s += (bfs(a))
    return s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s_count = int(input().strip())

    s = []

    for _ in range(s_count):
        s_item = input()
        s.append(s_item)

    y = kingdomino(s)

    fptr.write(str(y) + '\n')

    fptr.close()

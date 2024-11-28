#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import product

def make_tupledict(matrix, rows, cols):
    """Converts a matrix (in list of lists form) to a dictionary with tuples
    as keys.
    
    Arguments:
        matrix {List[List[int | float]]} -- matrix as list of lists (row-major order).
        rows {List[Any]} -- list of row keys.
        cols {List[Any]} -- list of column keys.
    
    Returns:
        Dict[Tuple[Any, Any], int|float] -- dictionary indexed by (row_key, col_key)
        tuples.
    """
    d = {}
    for r, row in enumerate(matrix):
        for c, item in enumerate(row):
            d[rows[r], cols[c]] = item
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
    
    if tiles[start_position] == 0:
        available.remove((cx, cy))
        return 0
    print()
    print('Starting', start_position)
    total_sa = 0
    while to_check:
        cx, cy = to_check.pop()
        try:
            available.remove((cx, cy))
        except Exception:
            pass
        print('checking', cx, cy)
        x,y = cx, cy
        this_height = tiles[x, y]
        total_height_differences = 0
        for xs, ys in shifts:
            try:
                nx, ny = x + xs, y + ys
                total_height_differences += max(this_height - tiles[nx, ny], 0)
                if (nx, ny) in available and tiles[(nx, ny)] != 0:
                    to_check.append((nx, ny))
                print(xs, ys, )
            except Exception:
                continue
        total_sa += total_height_differences + 2
        print('total', total_height_differences)
    print('SA', total_sa)
    return total_sa

def maxIslandSurfaceArea(t):
    from collections import defaultdict
    global tiles, available
    length = len(t)
    # YOUR SOLUTION HERE
    tiles = (make_tupledict(t, list(range(length)), list(range(length)) ))
    print(tiles)
    
    available = set(tiles.keys())
    tiles = defaultdict(lambda: 0, tiles)
    s = []
    while available:
        a = next(iter(available))
        # print(a)
        s.append(bfs(a))
    return max(s)

    # YOUR SOLUTION HERE

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rowCount = int(input().strip())

    columnCount = int(input().strip())

    islandGraph = []

    for _ in range(rowCount):
        islandGraph.append(list(map(int, input().rstrip().split())))

    maxSurfaceArea = maxIslandSurfaceArea(islandGraph)

    fptr.write(str(maxSurfaceArea) + '\n')

    fptr.close()

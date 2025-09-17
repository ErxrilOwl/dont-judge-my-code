#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    unique_minerals = {}
        
    for rock in arr:
        unique_minerals = set(rock).union(unique_minerals)

    record = {}
    for m in unique_minerals:
        record[m] = 0

    for rock in arr:
        for m in unique_minerals:
            if m in rock:
                record[m] += 1

    count = 0
    for m in unique_minerals:
        if record[m] == len(arr):
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    max_so_far_con = -sys.maxsize - 1
    current_max_con = 0
    
    max_non_con = 0
    has_positive = False
    max_negative = -sys.maxsize - 1
    
    for x in arr:
        current_max_con += x
        if max_so_far_con < current_max_con:
            max_so_far_con = current_max_con
        if current_max_con < 0:
            current_max_con = 0
            
        if x > 0:
            max_non_con += x
            has_positive = True
        if x < 0 and x > max_negative:
            max_negative = x
            
    if max_so_far_con == 0 and any(x < 0 for x in arr):
        max_so_far_con = max(arr)
        
    if not has_positive:
        max_non_con = max_negative
        
    return [max_so_far_con, max_non_con]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
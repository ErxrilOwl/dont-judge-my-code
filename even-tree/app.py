#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**6)

def evenForest(t_nodes, t_edges, t_from, t_to):
    children = [[] for _ in range(t_nodes)]
    for u, v in zip(t_from, t_to):
        children[v - 1].append(u - 1)

    subtree_sizes = [0] * t_nodes

    def dfs(node):
        if not children[node]:
            subtree_sizes[node] = 1
            return 1
        total = 0
        for child in children[node]:
            total += dfs(child)
        subtree_sizes[node] = total + 1
        return subtree_sizes[node]

    dfs(0)

    result = 0
    for i in range(1, t_nodes):
        if subtree_sizes[i] % 2 == 0:
            result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()

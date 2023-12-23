#!/usr/bin/env python3

import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)

grid = open(0).read().splitlines()

start = (0, 1)

# graph = defaultdict(list)


def neighbors(i, j):
    for ii in [-1, 1]:
        if 0 <= i + ii < len(grid):
            if grid[i + ii][j] != "#":
                yield i + ii, j
    for jj in [-1, 1]:
        if 0 <= j + jj < len(grid[i]):
            if grid[i][j + jj] != "#":
                yield i, j + jj


seen = set()


def find(from_, i, j):
    d = 1
    n = list(neighbors(i, j))
    while len(n) == 2:
        n.remove(from_)
        from_ = i, j
        i, j = n[0]
        print(i, j)
        d += 1
        n = list(neighbors(i, j))
    return (i, j), d


graph = defaultdict(list)


def build_graph():
    q = deque([(0, 1)])
    while q:
        (i, j) = q.popleft()
        if (i, j) in graph:
            continue
        n = list(neighbors(i, j))
        print(i, j, len(n))
        if len(n) > 2 or len(n) == 1:
            for ii, jj in n:
                next_, d = find((i, j), ii, jj)
                q.append(next_)
                graph[(i, j)].append((next_, d))


build_graph()
print(graph)
print(len(graph))


def dfs(node):
    if node[0] == len(grid) - 1:
        return 0
    if node in seen:
        return -1000000000000000000
    seen.add(node)
    rv = max((dfs(n) + d for n, d in graph[node]), default=-1000000)
    seen.remove(node)
    return rv


print(dfs(start))

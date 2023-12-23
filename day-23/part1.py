#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**6)

grid = open(0).read().splitlines()

start = (0, 1)


def neighbors(i, j):
    for ii in [-1, 1]:
        if 0 <= i + ii < len(grid):
            yield i + ii, j
    for jj in [-1, 1]:
        if 0 <= j + jj < len(grid[i]):
            yield i, j + jj


seen = set()


def dfs(i, j):
    if i == len(grid) - 1:
        return 0
    if (i, j) in seen:
        return -1
    seen.add((i, j))
    c = grid[i][j]
    if c == "#":
        return -1
    elif c == ">":
        rv = 1 + dfs(i, j + 1)
    elif c == "<":
        rv = 1 + dfs(i, j - 1)
    elif c == "v":
        rv = 1 + dfs(i + 1, j)
    elif c == "^":
        rv = 1+dfs(i - 1, j)
    else:
        rv = 1 + max(dfs(ii, jj) for ii, jj in neighbors(i, j))
    seen.remove((i, j))
    return rv


print(dfs(*start))

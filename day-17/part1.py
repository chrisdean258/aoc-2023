#!/usr/bin/env python3

from heapq import heappop, heappush

import numpy as np

g = []
for line in open(0):
    g.append([int(a) for a in line.strip()])


def add_pos(p, d):
    return p[0] + d[0], p[1] + d[1]


grid = np.array(g)


def in_grid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


seen = {}


def search():
    m = 10000000000000
    s = [(0, (0, 0), (0, 3, 0, 3))]
    seen = {}
    while s:
        cost_so_far, position, allowed = heappop(s)
        if cost_so_far > m:
            continue
        if position == (len(grid) - 1, len(grid[-1]) - 1):
            m = min(cost_so_far + grid[position], m)
            continue
        i, j = position
        up, down, left, right = allowed
        cost_so_far += grid[i][j]
        if (position, allowed) in seen:
            if cost_so_far < seen[(position, allowed)]:
                seen[(position, allowed)] = cost_so_far
            else:
                continue
        else:
            seen[(position, allowed)] = cost_so_far
        if up:
            if in_grid(i - 1, j):
                heappush(s, (cost_so_far, (i - 1, j), (up - 1, 0, 3, 3)))
        if down:
            if in_grid(i + 1, j):
                heappush(s, (cost_so_far, (i + 1, j), (0, down - 1, 3, 3)))
        if left:
            if in_grid(i, j - 1):
                heappush(s, (cost_so_far, (i, j - 1), (3, 3, left - 1, 0)))
        if right:
            if in_grid(i, j + 1):
                heappush(s, (cost_so_far, (i, j + 1), (3, 3, 0, right - 1)))
    return m


print(search() - grid[0][0])

#!/usr/bin/env python3

from contextlib import suppress
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


def search():
    m = 10000000000000
    s = [(0, (0, 0), (1, 1))]
    seen = {}
    while s:
        cost_so_far, position, allowed = heappop(s)
        if not in_grid(*position):
            continue
        # print(cost_so_far, position, allowed)
        if cost_so_far > m:
            continue
        if position == (len(grid) - 1, len(grid[-1]) - 1):
            return cost_so_far
        i, j = position
        ud, lr = allowed
        if seen.setdefault((position, allowed), cost_so_far) < cost_so_far:
            continue
        else:
            seen[(position, allowed)] = cost_so_far
        if ud:
            with suppress(IndexError):
                cc = cost_so_far
                for di in range(1, 10 + 1):
                    cc += grid[i - di][j]
                    if di >= 4:
                        heappush(s, (cc, (i - di, j), (0, 1)))
        if ud:
            with suppress(IndexError):
                cc = cost_so_far
                for di in range(1, 10 + 1):
                    cc += grid[i + di][j]
                    if di >= 4:
                        heappush(s, (cc, (i + di, j), (0, 1)))
        if lr:
            with suppress(IndexError):
                cc = cost_so_far
                for dj in range(1, 10 + 1):
                    cc += grid[i][j - dj]
                    if dj >= 4:
                        heappush(s, (cc, (i, j - dj), (1, 0)))
        if lr:
            with suppress(IndexError):
                cc = cost_so_far
                for dj in range(1, 10 + 1):
                    cc += grid[i][j + dj]
                    if dj >= 4:
                        heappush(s, (cc, (i, j + dj), (1, 0)))
    return m


print(search())

#!/usr/bin/env python3

from part1 import dists, grid

s = 0
for i, line in enumerate(grid):
    inside = False
    for j, c in enumerate(line):
        if (i, j) in dists:
            if grid[i][j] in "|LJS":
                inside = not inside
        else:
            s += inside

print(s)

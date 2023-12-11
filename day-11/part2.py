#!/usr/bin/env python3

grid = open(0).read().splitlines()

empty_lines = []
for i, line in enumerate(grid):
    if line.find("#") == -1:
        empty_lines.append(i)


empty_cols = []
for j in range(len(grid[0])):
    for i in range(len(grid)):
        if grid[i][j] == '#':
            break
    else:
        empty_cols.append(j)


def find_num_between(l, v1, v2):
    mi = min(v1, v2)
    ma = max(v1, v2)
    s = 0
    for val in l:
        if mi == val or val == ma:
            print("error")
        if mi < val < ma:
            s += 1
    return s * (1000000-1)


galaxies = []
for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == "#":
            galaxies.append((i, j))


s = 0
for i, g1 in enumerate(galaxies):
    for g2 in galaxies[i+1:]:
        s += abs(g1[0] - g2[0]) + find_num_between(empty_lines, g1[0], g2[0])
        s += abs(g1[1] - g2[1]) + find_num_between(empty_cols, g1[1], g2[1])
print(s)

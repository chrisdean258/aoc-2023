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

for i in reversed(empty_lines):
    grid.insert(i, "." * len(grid[0]))

for j in reversed(empty_cols):
    for i in range(len(grid)):
        grid[i] = grid[i][:j] + "." + grid[i][j:]

galaxies = []
for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == "#":
            galaxies.append((i, j))

s = 0
for i, g1 in enumerate(galaxies):
    for g2 in galaxies[i+1:]:
        s += abs(g1[0] - g2[0])
        s += abs(g1[1] - g2[1])
print(s)

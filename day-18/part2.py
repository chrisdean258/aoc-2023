#!/usr/bin/env python3

import numpy as np

dirs = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

dir_lookup = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}

pts = [(0, 0)]
position = (0, 0)
instrs = []
pdirs = {}
xs = set()
ys = set()
line_area = 0
for line in open(0):
    xs.add(position[0]-1)
    xs.add(position[0])
    xs.add(position[0]+1)
    ys.add(position[1]-1)
    ys.add(position[1])
    ys.add(position[1]+1)
    dir_, num, color = line.split()
    dir_ = dir_lookup[color[-2]]
    instrs.append((dir_, num))
    pts.append(position)
    pdirs[position] = dir_
    num = int(color[2:-2], 16)
    dir_ = dirs[dir_]
    position = (position[0] + dir_[0] * num, position[1] + dir_[1] * num)
    line_area += num

iss = sorted(xs)
jss = sorted(ys)

grid = np.zeros((len(iss) - 1, len(jss) - 1), dtype=int)
vals = grid.copy()

li = []
for i, ni in zip(iss, iss[1:]):
    li.append(ni - i)

for j in range(vals.shape[1]):
    vals[..., j] = np.array(li)

li = []
for i, ni in zip(jss, jss[1:]):
    li.append(ni - i)

for i in range(vals.shape[0]):
    vals[i] *= np.array(li)


i = iss.index(0)
j = jss.index(0)


for point in (pts[1:] + [pts[0]]):
    while iss[i] > point[0]:
        i -= 1
        grid[i][j] = 1
    while iss[i] < point[0]:
        i += 1
        grid[i][j] = 1
    while jss[j] < point[1]:
        j += 1
        grid[i][j] = 1
    while jss[j] > point[1]:
        j -= 1
        grid[i][j] = 1


s = 0
for i, line in enumerate(grid):
    inside = 0
    for j, is_line in enumerate(line):
        if inside or is_line:
            s += vals[i, j]
        if grid[i][j] and grid[i-1][j]:
            inside = not inside
print(s)

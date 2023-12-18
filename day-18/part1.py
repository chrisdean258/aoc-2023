#!/usr/bin/env python3

dirs = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0),
}

seen = set([(0, 0)])
position = [0, 0]
for line in open(0):
    dir_, num, color = line.split()
    num = int(num)
    dir_ = dirs[dir_]
    for _ in range(num):
        position[0] += dir_[0]
        position[1] += dir_[1]
        seen.add(tuple(position))

maxs = [0, 0]
mins = [0, 0]
for i, j in seen:
    if i < mins[0]:
        mins[0] = i
    if i > maxs[0]:
        maxs[0] = i
    if j < mins[1]:
        mins[1] = j
    if j > maxs[1]:
        maxs[1] = j

s = 0
for i in range(mins[0], maxs[0] + 1):
    inside = False
    for j in range(mins[1], maxs[1] + 1):
        if inside or (i, j) in seen:
            s += 1
        if (i, j) in seen and (i-1, j) in seen:
            inside = not inside
print(s)


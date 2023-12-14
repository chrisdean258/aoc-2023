#!/usr/bin/env python3

grid = open(0).read().splitlines()

s = 0
for j in range(len(grid[0])):
    c = 0
    p = 0
    for i in range(len(grid)):
        if grid[i][j] == "#":
            s += (len(grid) - p + 1) * c - c * (c + 1) // 2
            print(s)
            c = 0
            p = i + 1
        if grid[i][j] == "O":
            c += 1
    s += (len(grid) - (p - 1)) * c - c * (c + 1) // 2
    print(s)
    print()

print(s)

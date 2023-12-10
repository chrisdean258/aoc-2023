#!/usr/bin/env python3

from collections import deque

grid = open(0).read().splitlines()


for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == "S":
            start = (i, j)
            break

dists = {}
q = deque([(start, 0)])

while q:
    (i, j), d = q.popleft()
    try:
        c = grid[i][j]
    except:
        continue
    if (i, j) in dists:
        continue

    if c == 'S':
        if grid[i-1][j] in '|7F':
            q.append(((i - 1, j), d+1))
        if grid[i+1][j] in '|JL':
            q.append(((i + 1, j), d+1))
        if grid[i][j-1] in '-FL':
            q.append(((i, j - 1), d+1))
        if grid[i][j+1] in '-7J':
            q.append(((i, j + 1), d+1))

        if grid[i-1][j] in '|7F':
            if grid[i][j-1] in '-FL':
                # J
                grid[i] = grid[i].replace("S", "J")
            if grid[i][j+1] in '-7J':
                grid[i] = grid[i].replace("S", "L")
                # L
        if grid[i+1][j] in '|JL':
            if grid[i][j-1] in '-FL':
                grid[i] = grid[i].replace("S", "7")
                # 7
            if grid[i][j+1] in '-7J':
                grid[i] = grid[i].replace("S", "F")
                # F


    elif c == '|':
        q.append(((i - 1, j), d+1))
        q.append(((i + 1, j), d+1))
    elif c == '-':
        q.append(((i, j - 1), d+1))
        q.append(((i, j + 1), d+1))
    elif c == 'L':
        q.append(((i - 1, j), d+1))
        q.append(((i, j + 1), d+1))
    elif c == 'J':
        q.append(((i - 1, j), d+1))
        q.append(((i, j - 1), d+1))
    elif c == '7':
        q.append(((i + 1, j), d+1))
        q.append(((i, j - 1), d+1))
    elif c == 'F':
        q.append(((i + 1, j), d+1))
        q.append(((i, j + 1), d+1))

    dists[(i, j)] = d

print(max(dists.values()))

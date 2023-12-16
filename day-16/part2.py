#!/usr/bin/env python3

from collections import deque

grid = open(0).read().splitlines()


def energize(position, direction):
    q = deque([(position, direction)])
    while q:
        position, direction = q.popleft()
        if (position, direction) in seen:
            continue
        seen.add((position, direction))
        i, j = position
        di, dj = direction
        i += di
        j += dj
        if not (0 <= i < len(grid) and 0 <= j < len(grid[i])):
            continue
        c = grid[i][j]
        if c == ".":
            q.append(((i, j), direction))
        if c == "/":
            q.append(((i, j), (-dj, -di)))
        if c == "\\":
            q.append(((i, j), (dj, di)))
        if c == "|":
            if direction[0] == 0:
                q.append(((i, j), (1, 0)))
                q.append(((i, j), (-1, 0)))
            else:
                q.append(((i, j), direction))
        if c == "-":
            if direction[1] == 0:
                q.append(((i, j), (0, 1)))
                q.append(((i, j), (0, -1)))
            else:
                q.append(((i, j), direction))


m = 0
for i in range(len(grid)):
    seen = set()
    energize((i, -1), (0, 1))
    seen = {a for a, b in seen}
    m = max(m, len(seen) - 1)
    seen = set()
    energize((i, len(grid[0])), (0, -1))
    seen = {a for a, b in seen}
    m = max(m, len(seen) - 1)

for j in range(len(grid[0])):
    seen = set()
    energize((-1, j), (1, 0))
    seen = {a for a, b in seen}
    m = max(m, len(seen) - 1)
    seen = set()
    energize((len(grid), j), (-1, 0))
    seen = {a for a, b in seen}
    m = max(m, len(seen) - 1)

print(m)

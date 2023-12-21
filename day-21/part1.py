#!/usr/bin/env python3

grid = open(0).read().splitlines()


def neighbors(i, j):
    for ii in [-1, 1]:
        yield ((i + ii) % len(grid), j)
    for jj in [-1, 1]:
        yield (i, (j + jj) % len(grid[i]))


for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == "S":
            start = (i, j)
            break


prev = set([start])
evens = set(prev)
odds = set()
for i in range(64):
    if i % 2 == 0:
        evens |= prev
    else:
        odds |= prev
    possible = set()
    for i, j in prev:
        for ii, jj in neighbors(i, j):
            if grid[ii][jj] != "#" and (ii, jj) not in evens and (ii, jj) not in odds:
                possible.add((ii, jj))
    prev = possible
    if not prev:
        break


print(len(prev | evens))

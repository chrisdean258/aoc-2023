#!/usr/bin/env python3

from collections import defaultdict
from pprint import pprint

grid = open(0).read().splitlines()


def neighbors(i, j):
    for ii in [-1, 1]:
        yield (i + ii, j)
    for jj in [-1, 1]:
        yield (i, j + jj)


def neighbors1(i, j):
    for ii in [-1, 1]:
        yield ((i + ii) % len(grid), j)
    for jj in [-1, 1]:
        yield (i, (j + jj) % len(grid[i]))


for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c == "S":
            start = (i, j)
            break


target = 26501365
n = len(grid)

pppp = -1000
pp = 0
ppp = 0
double_prev = set()
prev = set([start])
evens = set(prev)
odds = set()
for i in range(10000):
    if i % 2 == 0:
        evens |= prev
    else:
        odds |= prev
        p = len(odds)
        if i % n == target % n:
            print(i, p, p - pp, (p - 2 * pp + ppp))
            if (p - 2 * pp + ppp) == pppp:
                a = pppp
                b = p - pp
                c = p
                break
            pppp = (p - 2 * pp + ppp)
            ppp = pp
            pp = p
    possible = set()
    for i, j in prev:
        for ii, jj in neighbors(i, j):
            if grid[ii % n][jj % n] != "#" and (ii, jj) not in double_prev:
                possible.add((ii, jj))
    double_prev = prev
    prev = possible

for away in range(-5, 5):
    print(away * 2 * n + i, a * away * (away + 1) // 2 + b * away + c)
away = (target - i) // (2 * n)
print(away * 2 * n + i, a * away * (away + 1) // 2 + b * away + c)
# away = 2

#!/usr/bin/env python3


grid = open(0).read().splitlines()


def neighbors(i, j):
    return [
        (i + 1, j),
        (i - 1, j),
        (i, j + 1),
        (i, j - 1)
    ]


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
double_prev = {}
prev = {start: None}
p = 0
tmn = target % n
for i in range(10000):
    if i % 2 == 1:
        p += len(prev)
        if i % n == tmn:
            if (p - 2 * pp + ppp) == pppp:
                a = pppp
                b = p - pp
                c = p
                break
            pppp = (p - 2 * pp + ppp)
            ppp = pp
            pp = p
    possible = {}
    for i, j in prev:
        for ii, jj in neighbors(i, j):
            if (ii, jj) not in double_prev:
                if grid[ii % n][jj % n] != "#":
                    possible[(ii, jj)] = None
    double_prev = prev
    prev = possible

# for away in range(-5, 5):
    # print(away * 2 * n + i, a * away * (away + 1) // 2 + b * away + c)
away = (target - i) // (2 * n)
print(away * 2 * n + i, a * away * (away + 1) // 2 + b * away + c)
# away = 2

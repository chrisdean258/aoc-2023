#!/usr/bin/env python3

from fractions import Fraction

import numpy as np

drops = []
for line in open(0).read().splitlines():
    line = line.replace(",", "").replace("@", "")
    drops.append([int(a) for a in line.split()])


def std(x, y, vx, vy):
    m = Fraction(vy, vx)
    return (-m, Fraction(1)), y - m * x


def when(p, x, y, dx, dy):
    return Fraction(p[0] - x, dx)


def solve(a, c):
    den = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if den == 0:
        return None
    xnum = c[0] * a[1][1] - a[0][1] * c[1]
    ynum = c[1] * a[0][0] - a[1][0] * c[0]
    return np.array([xnum / den, ynum / den])


s = 0
for i, drop in enumerate(drops):
    x, y, _, vx, vy, _ = drop
    std1, std13 = std(x, y, vx, vy)
    for other_drop in drops[i:]:
        xx, yy, _, vxx, vyy, _ = other_drop
        std2, std23 = std(xx, yy, vxx, vyy)
        a = np.array([std1, std2])
        b = np.array([std13, std23])
        p = solve(a, b)
        if p is None:
            continue
        if not ((200000000000000 <= p).all() and (400000000000000 >= p).all()):
            continue
        t1 = when(p, x, y, vx, vy)
        if t1 >= 0:
            s += when(p, xx, yy, vxx, vyy) >= 0
print(s)

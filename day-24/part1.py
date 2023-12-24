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
    test = Fraction(p[0] - x, dx)
    test2 = Fraction(p[1] - y, dy)
    assert abs(test - test2) < 1, f"{test} == {test2}"
    return test


def det(a):
    return a[0][0] * a[1][1] - a[1][0] * a[0][1]


def solve(a, b):
    d = 1 / det(a)
    inv = np.array([[a[1][1] * d, -a[0][1] * d], [-a[1][0] * d, a[0][0] * d]])
    return inv @ b.T


s = 0
for i, drop in enumerate(drops):
    x, y, _, vx, vy, _ = drop
    std1, std13 = std(x, y, vx, vy)
    for other_drop in drops[i:]:
        xx, yy, _, vxx, vyy, _ = other_drop
        std2, std23 = std(xx, yy, vxx, vyy)
        a = np.array([std1, std2])
        b = np.array([std13, std23])
        if det(a) == 0:
            continue
        p = solve(a, b)
        if not ((200000000000000 <= p).all() and (400000000000000 >= p).all()):
            continue
        t1 = when(p, x, y, vx, vy)
        t2 = when(p, xx, yy, vxx, vyy)
        if t1 >= 0 and t2 >= 0:
            s += 1
print(s)

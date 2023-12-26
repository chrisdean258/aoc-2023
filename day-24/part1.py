#!/usr/bin/env python3

from fractions import Fraction

drops = []
for line in open(0).read().splitlines():
    line = line.replace(",", "").replace("@", "")
    drops.append([int(a) for a in line.split()])

lb = 200000000000000
ub = 400000000000000
# lb = 7
# ub = 27

s = 0
for i, drop in enumerate(drops):
    x1, y1, _, vx1, vy1, _ = drop
    for other_drop in drops[i:]:
        x2, y2, _, vx2, vy2, _ = other_drop
        den = vx2*vy1 - vy2*vx1
        if den == 0:
            continue
        num = vy2 * vx1 * (x1 - x2) + vx2 * vx1 * (y2 - y1) + x1 * den
        x = Fraction(num, den)
        t1 = (x - x1) / vx1
        t2 = (x - x2) / vx2
        if t1 < 0 or t2 < 0:
            continue
        y_1 = y1 + t1 * vy1
        s += lb <= x <= ub and lb <= y_1 <= ub

print(s)

#!/usr/bin/env python3


drops = []
for line in open(0).read().splitlines():
    line = line.replace(",", "").replace("@", "")
    drops.append([int(a) for a in line.split()])

lb = 200000000000000
ub = 400000000000000

s = 0
for i, drop in enumerate(drops):
    x1, y1, _, vx1, vy1, _ = drop
    for other_drop in drops[i:]:
        x2, y2, _, vx2, vy2, _ = other_drop
        xden = vx2*vy1 - vy2*vx1
        if xden == 0:
            continue
        xnum = vy2 * vx1 * (x1 - x2) + vx2 * vx1 * (y2 - y1) + x1 * xden
        if xden < 0:
            xden = -xden
            xnum = -xnum

        t1n = xnum - x1 * xden
        t1d = vx1 * xden

        if t1d < 0:
            t1d = -t1d
            t1n = -t1n

        t2n = xnum - x2 * xden
        t2d = vx2 * xden
        if t2d < 0:
            t2d = -t2d
            t2n = -t2n

        if t1n < 0 or t2n < 0:
            continue

        y_1n = y1 * t1d + t1n * vy1
        y_1d = t1d
        if y_1d < 0:
            y_1d = -y_1d
            y_1n = -y_1n

        s += lb * xden <= xnum <= ub * xden and lb * y_1d <= y_1n <= ub * y_1d

print(s)

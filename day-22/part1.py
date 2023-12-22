#!/usr/bin/env python3


def min_max(a, b):
    return min(a, b), max(a, b)


bricks = []
for line in open(0).read().splitlines():
    b1, _, b2 = line.partition("~")
    b1 = [int(a) for a in b1.split(",")]
    b2 = [int(a) for a in b2.split(",")]
    bricks.append((b1, b2))

bricks.sort(key=lambda b: min(b[0][2], b[1][2]))

grid = {}
supporting = {}
supports = {i: [] for i in range(len(bricks))}

for i, ((b1x, b1y, b1z), (b2x, b2y, b2z)) in enumerate(bricks):
    minx, maxx = min_max(b1x, b2x)
    miny, maxy = min_max(b1y, b2y)
    minz, maxz = min_max(b1z, b2z)

    m = 0
    spts = set()
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            if (z := grid.get((x, y))):
                z, who = z
                if z > m:
                    m = z
                    spts = set([who])
                if z == m:
                    spts.add(who)

    m = maxz - minz + m + 1
    supporting[i] = spts
    for spt in spts:
        supports[spt].append(i)
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            grid[(x, y)] = (m, i)

s = 0
for brick, on_top in supports.items():
    for b2 in on_top:
        if len(supporting[b2]) == 1:
            break
    else:
        s += 1

print(s)

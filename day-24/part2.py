#!/usr/bin/env python3

from sympy import Matrix, solve, Symbol

drops = []
for line in open(0).read().splitlines():
    line = line.replace(",", "").replace("@", "")
    drops.append([int(a) for a in line.split()])


xx = Symbol("xx")
yy = Symbol("yy")
zz = Symbol("zz")
t1 = Symbol("t1")
t2 = Symbol("t2")
t3 = Symbol("t3")
vxx = Symbol("vxx")
vyy = Symbol("vyy")
vzz = Symbol("vzz")

a = solve(Matrix([drops[0][0] - xx - t1 * vxx - t1 * drops[0][3],
              drops[0][1] - yy - t1 * vyy - t1 * drops[0][4],
              drops[0][2] - zz - t1 * vzz - t1 * drops[0][5],
              drops[1][0] - xx - t2 * vxx - t2 * drops[1][3],
              drops[1][1] - yy - t2 * vyy - t2 * drops[1][4],
              drops[1][2] - zz - t2 * vzz - t2 * drops[1][5],
              drops[2][0] - xx - t3 * vxx - t3 * drops[2][3],
              drops[2][1] - yy - t3 * vyy - t3 * drops[2][4],
              drops[2][2] - zz - t3 * vzz - t3 * drops[2][5]]))[0]

print(a)
print(a[xx] + a[yy] + a[zz])

#!/usr/bin/env python3

from math import sqrt, ceil

a = open(0)
time = int(next(a).split(":")[1].replace(" ", ""))
record = int(next(a).split(":")[1].replace(" ", ""))
print(time, record)


# -t^2 + t * time - record

b = time
c = -record

t1 = int(ceil((b - sqrt(b*b + 4 * c)) / 2))
t2 = int((b + sqrt(b*b + 4 * c)) / 2)

print(t2 - t1 + 1)

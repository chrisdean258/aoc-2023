#!/usr/bin/env python3

a = open(0)
times = [int(b) for b in next(a).split(":")[1].split()]
records = [int(b) for b in next(a).split(":")[1].split()]


s = 1
for time, record in zip(times, records):
    ss = 0
    for i in range(time):
        distance = (time - i) * i
        if distance > record:
            ss += 1
    s *= ss
print(s)


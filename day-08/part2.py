#!/usr/bin/env python3

from itertools import cycle
from math import lcm

stdin = open(0)

instructions = cycle(next(stdin).strip())
starts = []
next(stdin)

network = {}

for line in stdin:
    node, _, steps = line.strip().partition(" = ")
    network[node] = steps[1:-1].split(", ")
    if node[-1] == "A":
        starts.append(node)

counts = []
for node in starts:
    count = 0
    while node[-1] != "Z":
        count += 1
        instruction = next(instructions)
        if instruction == "R":
            node = network[node][1]
        else:
            node = network[node][0]
    counts.append(count)

print(lcm(*counts))

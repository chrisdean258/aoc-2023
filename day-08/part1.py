#!/usr/bin/env python3

from itertools import cycle

stdin = open(0)

instructions = cycle(next(stdin).strip())
starts = []
next(stdin)

network = {}

for line in stdin:
    node, _, steps = line.strip().partition(" = ")
    network[node] = steps[1:-1].split(", ")

count = 0
node = "AAA"
while node != "ZZZ":
    count += 1
    instruction = next(instructions)
    if instruction == "R":
        node = network[node][1]
    else:
        node = network[node][0]
print(count)

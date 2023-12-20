#!/usr/bin/env python3

from collections import defaultdict, deque

inputs = defaultdict(list)
modules = {}
for line in open(0):
    name, effect = line.strip().split(" -> ")
    effect = effect.split(", ")
    if name == "broadcaster":
        broadcaster = [(e, "", "low") for e in effect]
    elif name[0] == "%":
        modules[name[1:]] = ["flipflop", effect, "off"]
    elif name[0] == "&":
        modules[name[1:]] = ["conjunction", effect, {}]
    for output_node in effect:
        inputs[output_node].append(name[1:])

print(inputs)

for name, (type_, _, _) in modules.items():
    if type_ == "conjunction":
        modules[name][2] = {n: "low" for n in inputs[name]}


low = 0
high = 0
for i in range(1000):
    low += 1
    q = deque(broadcaster)
    while q:
        to, from_, pulse = q.popleft()
        low += pulse == "low"
        high += pulse == "high"
        try:
            type_, output, state = modules[to]
        except KeyError:
            continue
        if type_ == "flipflop":
            if pulse == "low":
                if state == "on":
                    modules[to][2] = "off"
                    pulse = "low"
                if state == "off":
                    modules[to][2] = "on"
                    pulse = "high"
                for out in output:
                    q.append((out, to, pulse))
        else:
            state[from_] = pulse
            if all(s == "high" for s in state.values()):
                pulse = "low"
            else:
                pulse = "high"
            for out in output:
                q.append((out, to, pulse))

print(low * high)

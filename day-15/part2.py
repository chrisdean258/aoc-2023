#!/usr/bin/env python3

line = next(open(0)).strip()

boxes = [[] for _ in range(256)]


def find(box, label):
    for i, lense in enumerate(box):
        if lense[0] == label:
            return i
    return None


def hash(line):
    v = 0
    for c in line:
        v += ord(c)
        v *= 17
        v %= 256
    return v


for instr in line.split(","):
    label, cmd, _ = instr.partition('-')
    if '=' in instr:
        label, cmd, num = instr.partition("=")
        num = int(num)
    box = boxes[hash(label)]
    idx = find(box, label)
    if cmd == "=" and idx is not None:
        box[idx] = (label, num)
    elif cmd == "=":
        box.append((label, num))
    if cmd == "-" and idx is not None:
        del box[idx]

s = 0
for i, box in enumerate(boxes):
    for j, (label, power) in enumerate(box):
        s += (i + 1) * (j + 1) * power
print(s)

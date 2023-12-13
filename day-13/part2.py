#!/usr/bin/env python3

import numpy as np


def reflections(pattern, prev):
    for j in range(0, len(pattern)-1):
        ii = i = j + 1
        if i == prev:
            continue
        while j >= 0 and i < len(pattern):
            if (pattern[j] != pattern[i]).any():
                break
            i += 1
            j -= 1
        else:
            return ii
    return 0


patterns = []
p = []
for line in open(0):
    if len(line) == 1:
        patterns.append(np.array(p))
        p = []
    else:
        p.append(list(ord(a) for a in line.strip()))

patterns.append(np.array(p))

s = 0
for pattern in patterns:
    orig_row = reflections(pattern, -1)
    orig_col = reflections(pattern.T, -1)
    found = False
    for i in range(len(pattern)):
        if found:
            break
        for j in range(len(pattern[i])):
            if found:
                break
            pattern[i][j] ^= ord("#") ^ ord('.')
            row = reflections(pattern, orig_row)
            col = reflections(pattern.T, orig_col)
            s += 100 * row + col
            found = row or col
            pattern[i][j] ^= ord("#") ^ ord('.')


print(s)

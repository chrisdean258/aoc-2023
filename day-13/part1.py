#!/usr/bin/env python3

import numpy as np


def reflections(pattern):
    vals = []
    for i in range(0, len(pattern)-1):
        found = True
        ii = i
        j = i
        i += 1
        while j >= 0 and i < len(pattern):
            if (pattern[j] != pattern[i]).any():
                found = False
            i += 1
            j -= 1
        if found:
            vals.append(ii + 1)
    return vals


patterns = []
p = []
for line in open(0):
    if len(line) == 1:
        patterns.append(np.array(p))
        p = []
    else:
        p.append(list(line.strip()))

patterns.append(np.array(p))

s = 0
for pattern in patterns:
    rows = reflections(pattern)
    s += 100 * sum(rows)
    cols = reflections(pattern.T)
    s += sum(cols)

print(s)

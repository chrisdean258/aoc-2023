#!/usr/bin/env python3

import re

a = open(0)
workflows = {}
for line in a:
    line = line.strip()
    if line == "":
        break
    name, _, instrs = line.replace("}", "").partition("{")
    instrs = instrs.split(",")
    intp = []
    for instr in instrs[:-1]:
        instr = re.sub(r"([<>:])", r" \1 ", instr)
        part, comp, val, _colon, newwf = instr.split()
        val = int(val)
        intp.append((part, comp, val, newwf))

    workflows[name] = intp, instrs[-1]


def split(pl, ph, comp, val):
    if comp == "<":
        return (pl, val - 1), (val, ph)
    return (val + 1, ph), (pl, val)


def ssum(x):
    return x[1] - x[0] + 1


def evaluate(wf, x, m, a, s):
    if wf == "A":
        return ssum(x) * ssum(m) * ssum(a) * ssum(s)
    if wf == "R":
        return 0
    items, default = workflows[wf]
    ss = 0
    for part, comp, val, newwf in items:
        if part == "x":
            true_part, x = split(*x, comp, val)
            ss += evaluate(newwf, true_part, m, a, s)
        elif part == "m":
            true_part, m = split(*m, comp, val)
            ss += evaluate(newwf, x, true_part, a, s)
        elif part == "a":
            true_part, a = split(*a, comp, val)
            ss += evaluate(newwf, x, m, true_part, s)
        elif part == "s":
            true_part, s = split(*s, comp, val)
            ss += evaluate(newwf, x, m, a, true_part)
    ss += evaluate(default, x, m, a, s)
    return ss


ii = (1, 4000)
print(evaluate("in", ii, ii, ii, ii))

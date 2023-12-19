#!/usr/bin/env python3

a = open(0)
workflows = {}
for line in a:
    line = line.strip()
    if line == "":
        break
    name, _, instrs = line.replace("}", "").partition("{")
    instrs = instrs.split(",")
    workflows[name] = instrs


s = 0
for line in a:
    if line.strip() == "":
        break
    part = line.replace("{", "(").replace("}", ")")
    part = eval("dict" + part)

    wf = "in"
    while wf not in "AR":
        print(wf, end=" ")
        items = workflows[wf]
        for cond in items:
            if "<" in cond:
                key, _, rest = cond.partition("<")
                val, _, newwf = rest.partition(":")
                if part[key] < int(val):
                    wf = newwf
                    break
            elif ">" in cond:
                key, _, rest = cond.partition(">")
                val, _, newwf = rest.partition(":")
                if part[key] > int(val):
                    wf = newwf
                    break
            else:
                wf = cond
    print(part)
    print(wf)
    if wf == "A":
        s += sum(part.values())
print(s)

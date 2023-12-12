#!/usr/bin/env python3

import sys
from functools import lru_cache

sys.setrecursionlimit(10000)


@lru_cache
def possible(nums, line, must):
    if len(line) == 0 and len(nums) == 0:
        return 1
    if len(line) == 0 and nums == (0,):
        return 1
    if len(line) == 0:
        return 0
    if len(nums) == 0:
        return line.find("#") == -1
    if nums[0] == 0:
        if line[0] in '.?':
            return possible(nums[1:], line[1:], False)
        return 0
    if line[0] == '.' and not must:
        return possible(nums, line[1:], False)
    if line[0] == '#':
        nums2 = list(nums)
        nums2[0] -= 1
        return possible(tuple(nums2), line[1:], True)
    if line[0] == "?":
        s = 0 if must else possible(nums, '.' + line[1:], must)
        return s + possible(nums, '#' + line[1:], must)
    return 0


s = 0
for line in open(0):
    spring, cons = line.split(" ")
    nums = tuple(int(a) for a in cons.split(","))
    p = possible(nums, spring, False)
    print(nums, spring, p)
    s += p
print(s)

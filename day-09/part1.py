#!/usr/bin/env python3

def predict(nums):
    diffs = [b - a for (a, b) in zip(nums, nums[1:])]
    if all(d == 0 for d in diffs):
        return nums[-1]
    ld = predict(diffs)
    return nums[-1] + ld


s = 0
for line in open(0):
    nums = [int(a) for a in line.split()]
    print(predict(nums))
    s += predict(nums)
print(s)


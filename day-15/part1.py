#!/usr/bin/env python3

line = next(open(0)).strip()


def hash(line):
   v = 0
   for c in line:
        v += ord(c)
        v *= 17
        v %= 256
   return v


print(sum(map(hash, line.split(","))))

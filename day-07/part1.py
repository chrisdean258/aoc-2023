#!/usr/bin/env python3

from collections import Counter
from pprint import pprint

hands = []


def fixup(s):
    table = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    return tuple(int(table.get(c, c)) for c in s)


for line in open(0):
    hand, pts = line.split()
    pts = int(pts)
    hand = fixup(hand)
    c = Counter(hand).most_common()
    rank = c[0][1]
    if rank == 3 or rank == 2:
        if c[1][1] == 2:
            rank += 0.5
    hands.append((rank, hand, pts))

hands.sort()
pprint(hands)

s = 0
for i, hand in enumerate(hands, start=1):
    s += i * hand[2]

print(s)

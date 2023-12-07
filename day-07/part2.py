#!/usr/bin/env python3

from collections import Counter
from pprint import pprint

hands = []


def fixup(s):
    table = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    return tuple(int(table.get(c, c)) for c in s)


def score(hand):
    c = Counter(hand)
    try:
        ((mc, mcc), (smc, smcc)) = c.most_common(2)
    except:
        print( c.most_common(2))
        return 5

    if mc == 1 or smc == 1:
        return mcc + smcc
    return mcc + (0.5 if smcc == 2 else 0) + c[1]


for line in open(0):
    hand, pts = line.split()
    pts = int(pts)
    hand = fixup(hand)
    rank = score(hand)
    hands.append((rank, hand, pts))

hands.sort()
pprint(hands)

s = 0
for i, hand in enumerate(hands, start=1):
    s += i * hand[2]

print(s)

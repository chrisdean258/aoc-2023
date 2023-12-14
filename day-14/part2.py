#!/usr/bin/env python3

import numpy as np

grid = open(0).read().splitlines()
grid = np.array([[ord(a) for a in line] for line in grid])

seen = {}
seen_rev = []
counts = []


def interpret(grid):
    chars = []
    for line in grid:
        for c in line:
            chars.append(chr(c))
    return "".join(chars)


def count(grid):
    s = 0
    for i, line in enumerate(grid):
        for c in line:
            if c == ord("O"):
                s += len(grid) - i
    return s


def pprint(grid):
    for line in grid:
        for c in line:
            print(chr(c), end="")
        print()
    print()


def shift_up(grid):
    rows, cols = grid.shape
    for j in range(cols):
        p = 0
        for i in range(rows):
            if grid[i][j] == ord("#"):
                p = i + 1
            if grid[i][j] == ord("O"):
                grid[i][j] = ord(".")
                grid[p][j] = ord("O")
                p += 1
    return grid


for i in range(1000000000):
    seen_rev.append(grid.copy())
    counts.append(count(grid))
    grid = shift_up(grid)  # North
    grid = np.rot90(grid, axes=(1, 0))
    grid = shift_up(grid)  # West
    grid = np.rot90(grid, axes=(1, 0))
    grid = shift_up(grid)  # South
    grid = np.rot90(grid, axes=(1, 0))
    grid = shift_up(grid)  # East
    grid = np.rot90(grid, axes=(1, 0))
    rep = interpret(grid)
    if rep in seen:
        when = seen[rep]
        cycle_len = (i + 1 - when)
        final = (1000000000 - when) % cycle_len + when
        print(count(seen_rev[final]))
        break

    seen[rep] = i + 1

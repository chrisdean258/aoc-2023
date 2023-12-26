#!/usr/bin/env python3

import sys
from collections import defaultdict
from copy import deepcopy

sys.setrecursionlimit(10000)


def find_path(graph, src, sink, seen):
    if src in seen:
        return None
    seen.add(src)
    for node, v in graph[src].items():
        if v == 0:
            continue
        if node == sink:
            return [sink]
        if path := find_path(graph, node, sink, seen):
            path.append(node)
            return path
    return None


def ff(graph, src, sink):
    count = 0
    while True:
        seen = set()
        rev_path = find_path(graph, src, sink, seen)
        count += rev_path is not None
        if rev_path is None or count == 4:
            return count
        for n2, n1 in zip(rev_path, rev_path[1:]):
            graph[n1][n2] -= 1


def size(g, src):
    q = [src]
    seen = set()
    while q:
        node = q.pop()
        seen.add(node)
        for edge, v in g[node].items():
            if v != 0 and edge not in seen:
                q.append(edge)
    return len(seen)


graph = defaultdict(dict)
for line in open(0):
    line = line.replace(":", "")
    name, *cons = line.split()
    for con in cons:
        graph[name][con] = 1
        graph[con][name] = 1

nodes = list(graph.keys())

src = nodes[0]
for sink in nodes[1:]:
    g = deepcopy(graph)
    f = ff(g, src, sink)
    if f == 3:
        a = size(g, src)
        print(a * (len(g) - a))
        break

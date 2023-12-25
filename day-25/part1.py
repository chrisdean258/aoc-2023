#!/usr/bin/env python3

from collections import defaultdict, deque
from copy import deepcopy


def serialize(path):
    o = []
    while path:
        i, path = path
        o.append(i)
    return list(reversed(o))


def find_path(graph, src, sink):
    q = deque([(src, None)])
    seen = set()
    while q:
        node, parent = q.pop()
        if node == sink:
            return serialize((node, parent))
        seen.add(node)
        for n, v in graph[node].items():
            if n not in seen and v > 0:
                q.append((n, (node, parent)))


def ff(graph, src, sink):
    count = 0
    while path := find_path(graph, src, sink):
        count += 1
        if count == 4:
            return 4
        for n1, n2 in zip(path, path[1:]):
            graph[n1][n2] -= 1
            graph[n2][n1] += 1
    return count


def size(g, src):
    q = [src]
    seen = set()
    while q:
        node = q.pop()
        seen.add(node)
        for edge, v in g[node].items():
            if v > 0 and edge not in seen:
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

for i, src in enumerate(nodes):
    for sink in nodes[i + 1:]:
        g = deepcopy(graph)
        f = ff(g, src, sink)
        if f == 3:
            a = size(g, src)
            print(a* (len(g) - a))
            break
        else:
            continue
    else:
        continue
    break

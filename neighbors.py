import sys

def ImmediateNeighbors(pattern):
    neighbor = set()
    nuclset = ["A", "C", "G", "T"]
    for i in range(len(pattern)):
        for n in nuclset:
            neighbor.add(pattern[:i] + n + pattern[i + 1:])
    return neighbor


def Neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]
    ineighbor = ImmediateNeighbors(pattern)
    neighbor = ineighbor
    for x in range(d-1):
        for c in ineighbor:
            neighbor = neighbor.union(ImmediateNeighbors(p))
        ineighbor = neighbor
    return neighbor
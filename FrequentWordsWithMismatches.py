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

def ComputingFrequenciesWithMismatches(text, k, d):
    FrequencyArray = {}
    for i in range(0, len(text)-int(k)):
        pattern = text[i:i+k]
        Neighborhood = Neighbors(pattern, d)
        for n in Neighborhood:
            FrequencyArray[n] = FrequencyArray.get(n, 0) + 1
    m = max(FrequencyArray.values())
    return [t for t, v in counts.items() if v == m]

if __name__ = "__main__":
    print("Type in text, k and d!")
    data = list(sys.stdin().read().split().strip())
    text = data[0]
    k = data[1]
    d = data[2]
    print(ComputingFrequenciesWithMismatches(text, k, d))
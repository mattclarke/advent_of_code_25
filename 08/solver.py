import sys
import math


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [
    tuple([int(x) for x in line.strip().split(",")])
    for line in PUZZLE_INPUT.split("\n")
    if line
]

NUM_BOXES = len(lines)

distances = {}

for i, a in enumerate(lines):
    for j, b in enumerate(lines):
        if j <= i:
            continue
        dist = abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2 + abs(a[2] - b[2]) ** 2
        distances[math.sqrt(dist)] = (a, b)

ds = list(distances.keys())
ds.sort()

connections = {}

for d in ds[0:1000]:
    (a, b) = distances[d]
    x = connections.get(a, set())
    x.add(b)
    connections[a] = x
    x = connections.get(b, set())
    x.add(a)
    connections[b] = x

results = []
seen = set()

for k, v in connections.items():
    if k in seen:
        # Already part of a circuit
        continue
    nodes = set()
    q = [k]
    while q:
        a = q.pop(0)
        if a in nodes:
            continue
        nodes.add(a)
        seen.add(a)
        for n in connections[a]:
            q.append(n)
    results.append(len(nodes))

results.sort(reverse=True)

result = results[0] * results[1] * results[2]

# Part 1 = 129564
print(f"answer = {result}")

connections = {}
result = 0

for d in ds:
    (a, b) = distances[d]
    x = connections.get(a, set())
    x.add(b)
    connections[a] = x

    x = connections.get(b, set())
    x.add(a)
    connections[b] = x

    q = list(x)
    seen = {b}
    while q:
        n = q.pop(0)
        if n in seen:
            continue
        seen.add(n)
        for nn in connections[n]:
            q.append(nn)
    if len(seen) == NUM_BOXES:
        result = a[0] * b[0]
        break

# Part 2 = 42047840
print(f"answer = {result}")

# Internet solution using Kruskal's algorithm.


def find_subtree(parents, i):
    if parents[i] == i:
        return i
    return find_subtree(parents, parents[i])


pos_to_id = {}
parents = []
rank = []

for i, l in enumerate(lines):
    pos_to_id[l] = i
    parents.append(i)
    rank.append(0)

e = 0

for d in ds:
    (a, b) = distances[d]

    x = find_subtree(parents, pos_to_id[a])
    y = find_subtree(parents, pos_to_id[b])

    if x == y:
        # Forms a loop so reject
        continue
    e += 1
    if e == NUM_BOXES - 1:
        result = a[0] * b[0]
        break

    if rank[x] > rank[y]:
        parents[y] = x
    elif rank[y] > rank[x]:
        parents[x] = y
    else:
        parents[y] = x
        rank[x] += 1

print(f"answer = {result}")

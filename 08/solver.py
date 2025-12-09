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
# Consider nodes like the following:
#
# A  B  C
#
# D   E
#
# We need to connect them based on edge weights
# (for this puzzle, the weight is the distance between nodes).
#
# First we assign each node as its own parent and a rank 0
# Node:   A B C D E
# Parent: A B C D E
# Rank:   0 0 0 0 0
#
# Then for the lowest weight/distance we "join" two nodes
# by making one the parent of the other and increase the rank of the parent.
# For example: A and B
#
# Node:   A B C D E
# Parent: B B C D E
# Rank:   0 1 0 0 0
#
# Then repeat for the next lowest weight/distance.
# For example: A and C
# We recurse to find the parent of both nodes and for A this is B,
# so we attach C to B.
#
# Node:   A B C D E
# Parent: B B B D E
# Rank:   0 2 0 0 0
#
# The next lowest weight is B and C.
# Again we recurse to find the parents and they are both B,
# so we don't join them because this would create a loop.
#
# Then we try the next lowest which is D and E.
# Both are their own parents, so we join one to the other.
#
# Node:   A B C D E
# Parent: B B B E E
# Rank:   0 2 0 0 1
#
# Now we have two separate graphs.
# The next lowest weight is A and D.
# We recurse to find the parents (B and E) and join them.
#
# Node:   A B C D E
# Parent: B B B E B
# Rank:   0 3 0 0 1
#
# And we are done because we have all nodes connected and no loops.
# For all N nodes to be connected there will be N - 1 edges.
#
# Note: for this particular example the rank is not important.


def find_subtree(parents, i):
    if parents[i] == i:
        return i
    return find_subtree(parents, parents[i])


pos_to_id = {}
parent = []
rank = []

for i, l in enumerate(lines):
    pos_to_id[l] = i
    parent.append(i)
    rank.append(0)

joined_edges = 0

for d in ds:
    (a, b) = distances[d]

    x = find_subtree(parent, pos_to_id[a])
    y = find_subtree(parent, pos_to_id[b])

    if x == y:
        # Forms a loop so reject
        continue
    joined_edges += 1
    if joined_edges == NUM_BOXES - 1:
        result = a[0] * b[0]
        break

    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[y] > rank[x]:
        parent[x] = y
    else:
        parent[y] = x
        rank[x] += 1

print(f"answer = {result}")


import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

nodes = {}

for line in lines:
    parts = line.replace(":", "").split()
    nodes[parts.pop(0)] = parts

results = set()
Q = []
for x in nodes["you"]:
    Q.append((x, "you"))

while Q:
    curr, path = Q.pop(0)
    new_path = path + "," + curr
    if curr == "out":
        results.add(new_path)
        continue

    for v in nodes[curr]:
        if v not in new_path:
            Q.append((v, new_path))

# Part 1 = 534
print(f"answer = {len(results)}")

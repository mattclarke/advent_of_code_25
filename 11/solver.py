import sys


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

DP = {}


def recurse(curr, target):
    if curr in DP:
        return DP[curr]

    if curr == target:
        return 1

    count = 0

    if curr not in nodes:
        return 0

    for x in nodes[curr]:
        count += recurse(x, target)
    DP[curr] = count

    return count


recurse("svr", "fft")
result = DP["svr"]

DP.clear()

recurse("fft", "dac")
result *= DP["fft"]

DP.clear()

recurse("dac", "out")
result *= DP["dac"]

# Part 2 = 499645520864100
print(f"answer = {result}")

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

DP = {}


def internet_solution(curr, seen_fft, seen_dac):
    if curr == "out":
        return 1 if seen_fft and seen_dac else 0

    count = 0
    for x in nodes[curr]:
        new_fft = seen_fft or x == "fft"
        new_dac = seen_dac or x == "dac"

        if (x, new_fft, new_dac) in DP:
            res = DP[(x, new_fft, new_dac)]
        else:
            res = internet_solution(x, new_fft, new_dac)
            DP[(x, new_fft, new_dac)] = res
        count += res

    return count


print(f"answer = {internet_solution('svr', False, False)}")

import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

bales = set()

for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "@":
            bales.add((r, c))

result = 0

for (r, c) in bales:
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            if (r + dr, c + dc) in bales:
                count += 1
    if count < 4:
        result += 1

# Part 1 = 1604
print(f"answer = {result}")

num_bales = len(bales)

while True:
    to_remove = set()
    for (r, c) in bales:
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if (r + dr, c + dc) in bales:
                    count += 1
        if count < 4:
            to_remove.add((r, c))
    if not to_remove:
        break
    bales = bales.difference(to_remove)

result = num_bales - len(bales)

# Part 2 = 9397
print(f"answer = {result}")

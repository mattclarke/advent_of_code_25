import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line for line in PUZZLE_INPUT.split("\n") if line]
print(lines)

cols = []
for line in lines:
    for i, x in enumerate(line.strip().split()):
        if len(cols) <= i:
            cols.append([x])
            continue
        cols[i].append(x)

result = 0

for c in cols:
    op = c[~0]
    ans = int(c[0])
    for n in c[1:-1]:
        if op == "*":
            ans *= int(n)
        elif op == "+":
            ans += int(n)
        else:
            assert False
    result += ans


# Part 1 = 5667835681547
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")

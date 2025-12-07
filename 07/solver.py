import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0

start = lines[0].index("S")
beams = {start}

for line in lines[1:]:
    new_beams = set()
    for b in beams:
        if line[b] == "^":
            result += 1
            new_beams.add(b - 1)
            new_beams.add(b + 1)
        else:
            new_beams.add(b)
    beams = new_beams

# Part 1 = 1640
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")

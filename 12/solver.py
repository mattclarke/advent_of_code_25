import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n\n") if line]

SHAPES = []
AREAS = []
ALLOWED = []

for line in lines[:6]:
    slines = line.split("\n")
    shape = set()
    for r, sline in enumerate(slines[1:]):
        for c, ch in enumerate(sline):
            if ch == "#":
                shape.add((r, c))
    SHAPES.append(shape)

for line in lines[6].replace(":", "").split("\n"):
    parts = line.split(" ")
    area = tuple([int(x) for x in parts[0].split("x")])
    allowances = tuple([int(x) for x in parts[1:]])
    AREAS.append(area)
    ALLOWED.append(allowances)


result = 0

for sline in lines:
    pass

# Part 1 = 
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")

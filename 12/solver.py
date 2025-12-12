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


# Symmetry means we don't need to try every starting position and/or rotation?

def draw_shape(shape):
    for r in range(3):
        line = []
        for c in range(3):
            if (r, c) in shape:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))
    print("")


def rotate_right(shape):
    new_shape = set()
    if (0, 0) in shape:
        new_shape.add((0, 2))
    if (0, 1) in shape:
        new_shape.add((1, 2))
    if (0, 2) in shape:
        new_shape.add((2, 2))
    if (1, 0) in shape:
        new_shape.add((0, 1))
    if (1, 1) in shape:
        new_shape.add((1, 1))
    if (1, 2) in shape:
        new_shape.add((2, 1))
    if (2, 0) in shape:
        new_shape.add((0, 0))
    if (2, 1) in shape:
        new_shape.add((1, 0))
    if (2, 2) in shape:
        new_shape.add((2, 0))
    return new_shape


result = 0

for area, allowed in zip(AREAS, ALLOWED):
    allowed_shapes = []
    total_shape_area = 0
    for i, a in enumerate(allowed):
        allowed_shapes.extend([SHAPES[i]] * a)
        total_shape_area += len(SHAPES[i]) * a
    if total_shape_area > area[0] * area[1]:
        print("Not a chance")
        continue


# Part 1 = 
print(f"answer = {result}")

result = 0

# Part 2 = 
print(f"answer = {result}")

import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [
    tuple([int(x) for x in line.strip().split(",")])
    for line in PUZZLE_INPUT.split("\n")
    if line
]

result = 0
rects = []

for i, (ax, ay) in enumerate(lines):
    for j, (bx, by) in enumerate(lines):
        if j <= i:
            continue
        area = abs((ax - bx + 1) * (ay - by + 1))
        rects.append((area, (ax, ay), (bx, by)))
        result = max(result, area)

rects.sort(reverse=True)

# Part 1 = 4748769124
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")


def foo(data):
    for y in range(12):
        line = []
        for x in range(12):
            if (x,y) in data:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))
    print("======")


def find_line(a, b):
    line = set()
    (ax, ay) = a
    (bx, by) = b
    line.add((ax, ay))
    line.add((bx, by))
    if ax > bx:
        for j in range(bx, ax):
            line.add((j, ay))
    elif bx > ax:
        for j in range(ax, bx):
            line.add((j, ay))
    elif ay > by:
        for j in range(by, ay):
            line.add((ax, j))
    elif by > ay:
        for j in range(ay, by):
            line.add((ax, j))
    else:
        assert False
    return line


border = set()

for i, a in enumerate(lines[:-1]):
    b = lines[i+1]
    temp = find_line(a, b)
    border = border.union(temp)

# Join the loop
temp = find_line(lines[0], lines[~0])
border = border.union(temp)


result = 0

for i, (ax, ay) in enumerate(lines):
    for j, (bx, by) in enumerate(lines):
        pass

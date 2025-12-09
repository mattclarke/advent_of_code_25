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
        area = (abs(ax - bx) + 1) * (abs(ay - by) + 1)
        rects.append((area, (ax, ay), (bx, by)))
        result = max(result, area)


rects.sort(reverse=True)

# Part 1 = 4748769124
print(f"answer = {result}")


def join_tiles(a, b):
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
    b = lines[i + 1]
    temp = join_tiles(a, b)
    border = border.union(temp)

# Join the loop
temp = join_tiles(lines[0], lines[~0])
border = border.union(temp)

pruned = []

# Add the first tile to the end, so we can iterate over each "edge"
lines.append(lines[0])

for size, a, b in rects:
    valid = True
    ax, ay = a
    bx, by = b
    min_x = min(ax, bx)
    max_x = max(ax, bx)
    min_y = min(ay, by)
    max_y = max(ay, by)

    a = (min_x, min_y)
    b = (max_x, max_y)

    for tile in lines:
        tx, ty = tile
        if min_x < tx < max_x and min_y < ty < max_y:
            valid = False
            break
    if valid:
        pruned.append((size, a, b))


for size, a, b in pruned:
    valid = True
    ax, ay = a
    bx, by = b
    min_x = min(ax, bx)
    max_x = max(ax, bx)
    min_y = min(ay, by)
    max_y = max(ay, by)

    a = (min_x, min_y)
    b = (max_x, max_y)

    flines = lines[:]
    flines.append(lines[0])
    prev = flines[0]

    for tile in flines:
        if tile == prev:
            continue
        tx, ty = tile
        px, py = prev
        prev = tile

        if tx == px:
            # Vertical line
            if tx <= min_x or tx >= max_x:
                continue
            if py >= max_y and ty <= min_y:
                valid = False
            elif ty >= max_y and py <= min_y:
                valid = False
        else:
            # Horizontal line
            if ty <= min_y or ty >= max_y:
                continue
            if px >= max_x and tx <= min_x:
                valid = False
            elif tx >= max_x and px <= min_x:
                valid = False
        if not valid:
            break
    if valid:
        result = size
        break

# Part 2 = 1525991432
print(f"answer = {result}")

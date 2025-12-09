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

    # Set prev to the last tile, so we cover all edges.
    prev = lines[~0]

    for tile in lines:
        tx, ty = tile
        px, py = prev
        prev = tile

        # If the tile is in the rectange then it isn't valid.
        if min_x < tx < max_x and min_y < ty < max_y:
            valid = False
            break

        # Check to see if any "edges" cross the whole rectangle width-wise or height-wise.
        # If so, then the rectangle is not valid.
        if tx == px:
            # Vertical line
            if tx <= min_x or tx >= max_x:
                continue
            y1, y2 = min(py, ty), max(py, ty)
            if y2 >= max_y and y1 <= min_y:
                valid = False
        else:
            # Horizontal line
            if ty <= min_y or ty >= max_y:
                continue
            x1, x2 = min(px, tx), max(px, tx)
            if x2 >= max_x and x1 <= min_x:
                valid = False

    if valid:
        result = size
        break

# Part 2 = 1525991432
print(f"answer = {result}")

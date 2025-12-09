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

min_x = 10000000000000000000
min_y = 10000000000000000000

for i, (ax, ay) in enumerate(lines):
    for j, (bx, by) in enumerate(lines):
        if j <= i:
            continue
        if ax != bx:
            min_x = min(min_x, abs(ax-bx))
        if ay != by:
            min_y = min(min_y, abs(ay-by))
        area = (abs(ax - bx) + 1) * (abs(ay - by) + 1)
        rects.append((area, (ax, ay), (bx, by)))
        result = max(result, area)


rects.sort(reverse=True)
print(rects[0])

# Part 1 = 4748769124
print(f"answer = {result}")

result = 0

# Part 2 = 1525991432
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

red_tiles = set(lines)
tiles_x = []
tiles_y = []

for r in red_tiles:
    tiles_x.append(r[0])
    tiles_y.append(r[1])

print(len(red_tiles))

result = 0


pruned = []

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

    count = 0
    for tile in red_tiles:
        tx, ty = tile
        if min_x < tx < max_x and min_y < ty < max_y:
            count += 1
            break
    print(size, count)
    if count == 0:
        pruned.append((size, a, b))

print("pruned", len(pruned))

# pruned = [(30,(2, 5),(11, 7))]

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
    # print(min_x, max_x, min_y, max_y)

    flines = lines[:]
    flines.append(lines[0])
    prev = flines[0]

    for tile in flines:
        if tile == prev:
            continue
        tx, ty = tile
        px, py = prev
        # print(prev, tile)
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
        print("Valid", size, a, b)
        print((a[0] - b[0]+1)*(a[1]-b[1]+1)) 
        assert False




    # print(a, b)
    #
    # for x in range(min_x +1, max_x):
    #     if x not in tiles_x:
    #         continue
    #     for y in range(min_y + 1, max_y):
    #         if (x,y) in border:
    #             print("Fail", size)
    #             valid = False
    #             break
    #     if not valid:
    #         break
    # if not valid:
    #     continue
    # for y in range(min_y + 1, max_y):
    #     if y not in tiles_y:
    #         continue
    #     for x in range(min_x +1, max_x):
    #         if (x,y) in border:
    #             print("Fail", size)
    #             valid = False
    #             break
    #     if not valid:
    #         break
    #
    # if valid:
    #     print("Win", size)
    #     break

    # print(size, min_x, max_x, min_y, max_y)
    # start = lines.index(a)
    # next_red = (start + 1) % len(lines)
    # prev_x, prev_y = lines[start]
    # while next_red != start:
    #     nx, ny = lines[next_red]
    #     next_red = (next_red + 1) % len(lines)
    #
    #     between_x = min_x < nx < max_x
    #     between_y = min_y < ny < max_y
    #
    #     if between_x and between_y:
    #         valid = False
    #         break
    #
    #     y1, y2 = min(prev_y, ny), max(prev_y, ny)
    #     x1, x2 = min(prev_x, nx), max(prev_x, nx)
    #
    #     if between_x and y1 <= min_y < y2:
    #         valid = False
    #         break
    #
    #     if between_y and x1 <= min_x < x2:
    #         valid = False
    #         break
    #
    #     prev_x = nx
    #     prev_y = ny
    #
    # if valid:
    #     print(size)
    #     break


# 3621412687 is too high
# 1525957356 is wrong but I have got it multiple times!
# 1525778232
# 1525991432
# 1518085800  is too low

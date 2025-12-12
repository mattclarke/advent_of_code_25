import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n\n") if line]

SHAPES = []
INPUTS = []

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
    area = [int(x) for x in parts[0].split("x")]
    area = (min(area), max(area))
    allowances = tuple([int(x) for x in parts[1:]])
    min_shape = min(allowances)
    INPUTS.append((area, min_shape, allowances))


# Sort by width and secondarily min_shape
INPUTS.sort(key=lambda x: x[1])
INPUTS.sort(key=lambda x: x[0][0])


def draw(layout, nr, nc):
    for r in range(nr):
        line = []
        for c in range(nc):
            if (r, c) in layout:
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


CACHE = {}


def solve(shapes, num_r, num_c, min_shape, width_changed):
    if width_changed:
        CACHE.clear()

    def recurse(index, layout):
        if index == len(shapes):
            # draw(layout, num_r, num_c)
            # input()
            return True

        curr_shape = SHAPES[shapes[index]]

        if index == min_shape * len(SHAPES) and min_shape not in CACHE:
            CACHE[min_shape] = layout

        for rr in range(num_r):
            for cc in range(num_c):
                for rot in range(4):
                    new_layout = copy.copy(layout)
                    if rot > 0:
                        curr_shape = rotate_right(curr_shape)
                    # Does shape fit?
                    fit = True
                    for r, c in curr_shape:
                        if (rr + r, cc + c) in layout:
                            fit = False
                            break
                        if rr + r >= num_r:
                            fit = False
                            break
                        if cc + c >= num_c:
                            fit = False
                            break
                    if fit:
                        for r, c in curr_shape:
                            new_layout.add((rr + r, cc + c))
                        if recurse(index + 1, new_layout):
                            return True
        return False

    # Look in CACHE, so we can start from a known position
    entry = 0
    for k in sorted(CACHE):
        if k > min_shape:
            break
        entry = k

    if entry > 0:
        return recurse(min_shape * len(SHAPES), CACHE[entry])
    else:
        print("CACHE MISS")
        return recurse(0, set())


result = 0
last_width = 0

for (cols, rows), min_shape, allowed in INPUTS:
    allowed_shapes = []
    total_shape_area = 0
    for i in range(min_shape):
        allowed_shapes.append(0)
        total_shape_area += len(SHAPES[0])
        allowed_shapes.append(1)
        total_shape_area += len(SHAPES[1])
        allowed_shapes.append(2)
        total_shape_area += len(SHAPES[2])
        allowed_shapes.append(3)
        total_shape_area += len(SHAPES[3])
        allowed_shapes.append(4)
        total_shape_area += len(SHAPES[4])
        allowed_shapes.append(5)
        total_shape_area += len(SHAPES[5])
    for i, a in enumerate(allowed):
        allowed_shapes.extend([i] * (a - min_shape))
        total_shape_area += len(SHAPES[i]) * (a - min_shape)
    if total_shape_area > rows * cols:
        continue
    if solve(allowed_shapes, rows, cols, min_shape, last_width != cols):
        result += 1
        print(result)
    last_width = cols

# Part 1 = 437
print(f"answer = {result}")

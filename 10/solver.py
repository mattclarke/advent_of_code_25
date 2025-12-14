import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

input_data = []

for line in lines:
    parts = line.split()
    front = parts.pop(0).replace("[", "").replace("]", "")
    back = parts.pop().replace("{", "").replace("}", "")
    pattern = []
    for p in front:
        if p == "#":
            pattern.append(True)
        else:
            pattern.append(False)
    jolts = []
    for p in back.split(","):
        jolts.append(int(p))
    switches = []
    for p in parts:
        temp = []
        p = p.replace("(", "").replace(")", "")
        for x in p.split(","):
            temp.append(int(x))
        switches.append(tuple(temp))
    input_data.append((pattern, switches, jolts))


def bfs1(input_data):
    pattern, switches, _ = input_data
    state = [False for _ in pattern]
    Q = [(0, state)]
    # Don't revist seen states
    seen = set()
    while Q:
        depth, state = Q.pop(0)
        if tuple(state) in seen:
            continue
        seen.add(tuple(state))
        for s in switches:
            new_state = state.copy()
            for i in s:
                new_state[i] = not new_state[i]
            if new_state == pattern:
                return depth + 1
            Q.append((depth + 1, new_state))


result = 0

for data in input_data:
    result += bfs1(data)

# Part 1 = 505
print(f"answer = {result}")

# Puzzles are:
#     (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# First part can be written as:
#     (3)    => [0, 0, 0, 1]
#     (1, 3) => [0, 1, 0, 1]
#     ...
#     (0, 1) => [1, 1, 0, 0]
# So the puzzle is:
#     A x [0, 0, 0, 1] + B x [0, 1, 0, 1] + .. + F x [1, 1, 0, 0] = {3,5,4,7}
# To solve we need to find A, B, C, etc.
# If we group all that can contribute to 0 then:
#     E + F = 3
# Then for 1 we get:
#     B + F = 5
# For 2:
#     C + D + E = 4
# For 3:
#     A + B + D = 7
# That should help limit the options...
# But how to code it...
# Guess E = 2 => F = 1 => B = 4 => A + D = 3 => C + D = 2
# Guess D = 1 => A = 2 and C = 1
# 0 0 0 2
# 0 4 0 4
# 0 0 1 0
# 0 0 1 1
# 2 0 2 0
# 1 1 0 0
# -------
# 3 5 4 7 
# Correct but depth is 11, so there is a better solution...
#
# Try D = 2 => A = 1 and C = 0
# 0 0 0 1
# 0 4 0 4
# 0 0 0 0
# 0 0 2 2
# 2 0 2 0
# 1 1 0 0
# -------
# 3 5 4 7 
# Depth = 10 which is the lowest.


def is_valid(candidates, foo, jolts):
    for k, v in foo.items():
        incomplete = False
        bar = []
        for vv in v:
            if vv < len(candidates):
                bar.append(candidates[vv])
            else:
                incomplete = True
                break
        if incomplete:
            continue
        if sum(bar) != jolts[k]:
            return False
    return True


best = 1000000000000
    
def solve(foo, switches, jolts, maximums):
    global best
    def recurse(i, candidates):
        global best
        if not is_valid(candidates, foo, jolts):
            return
        if sum(candidates) >= best:
            return
        if len(candidates) == len(switches):
            best = min(best, sum(candidates))
            print(candidates, sum(candidates), best)
            return
        # print(i, candidates)
        for x in range(0, maximums[i] + 1):
            candidates.append(x)
            recurse(i+1, candidates)
            candidates.pop()
    best = 1000000000000
    recurse(0, [])
    print(best)
    return best

result = 0

for _, switches, jolts in input_data:
    foo = {x: set() for x in range(len(jolts))}
    for i, switch in enumerate(switches):
        for s in switch:
            foo[s].add(i)

    maximums = [10000 for _ in switches]
    for k, v in foo.items():
        for vv in v:
            maximums[vv] = min(maximums[vv], jolts[k])

    result += solve(foo, switches, jolts, maximums)

# Part 2 = 
print(f"answer = {result}")

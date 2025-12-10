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

result = 0

# Part 2 = 
print(f"answer = {result}")

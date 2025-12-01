import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0
pos = 50

for line in lines:
    d = line[0]
    n = int(line[1:])
    if d == "L":
        pos -= n
    else:
        pos += n
    pos %= 100
    if pos == 0:
        result += 1

# Part 1 = 1055
print(f"answer = {result}")

result = 0
pos = 50
prev = True

for line in lines:
    d = line[0]
    n = int(line[1:])
    for i in range(n):
        if d == "L":
            pos -= 1
        else:
            pos += 1
        pos %= 100
        if pos == 0:
            result += 1

# Part 2 = 6368
print(f"answer = {result}")

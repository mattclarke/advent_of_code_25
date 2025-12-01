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
    assert pos < 100
    assert pos >= 0

    d = line[0]
    n = int(line[1:])
    result += n // 100
    n = n % 100

    if d == "L":
        new_pos = pos - n
        if pos != 0 and new_pos <= 0:
            result += 1
        pos = new_pos % 100
    elif d == "R":
        new_pos = pos + n
        if new_pos > 99:
            result += 1
        pos = new_pos % 100

# Part 2 = 6368
print(f"answer = {result}")

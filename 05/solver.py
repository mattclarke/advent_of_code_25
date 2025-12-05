import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

parts = PUZZLE_INPUT.split("\n\n")

ranges = [
    [int(x) for x in line.strip().split("-")] for line in parts[0].split("\n")
]
items = [int(line.strip()) for line in parts[1].split("\n") if line]

result = 0

for item in items:
    for low, high in ranges:
        if low <= item <= high:
            result += 1
            break


# Part 1 = 848
print(f"answer = {result}")

result = 0
pos = 0

for low, high in sorted(ranges):
    if pos < low:
        result += high - low + 1
        pos = high
    elif pos < high:
        result += high - pos
        pos = high

# Part 2 = 334714395325710
print(f"answer = {result}")

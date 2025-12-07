import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

result = 0
start = lines[0].index("S")
beams = {start}

for line in lines[1:]:
    new_beams = set()
    for b in beams:
        if line[b] == "^":
            result += 1
            new_beams.add(b - 1)
            new_beams.add(b + 1)
        else:
            new_beams.add(b)
    beams = new_beams

# Part 1 = 1640
print(f"answer = {result}")

start = lines[0].index("S")
beams = {start}

DP = {}


def solve(ln, r):
    if ln == len(lines):
        return 1

    if lines[ln][r] == "^":
        if (ln, r) in DP:
            return DP[(ln, r)]
        ans = solve(ln + 1, r - 1) + solve(ln + 1, r + 1)
        DP[(ln, r)] = ans
        return ans
    else:
        return solve(ln + 1, r)


result = solve(1, start)

# Part 1 = 1640
print(f"answer = {len(DP)}")

# Part 2 = 40999072541589
print(f"answer = {result}")

# Internet solution - Pascal's triangle like solution
#          1
#         1^1
#         1 1
#        1^2^1
#        1 2 1
#       1^121^1
#       1 121 1
#      1^2^311^1
start = lines[0].index("S")
beams = {start: 1}

for line in lines[1:]:
    next_beams = {}
    for b, c in beams.items():
        if line[b] == "^":
            x = next_beams.get(b - 1, 0)
            next_beams[b - 1] = x + c
            x = next_beams.get(b + 1, 0)
            next_beams[b + 1] = x + c
        else:
            x = next_beams.get(b, 0)
            next_beams[b] = x + c
    beams = next_beams

# Part 2 = 40999072541589
print(f"answer = {sum(beams.values())}")

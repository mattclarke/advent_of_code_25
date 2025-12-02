import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
lines = lines[0].split(",")

result = 0

for line in lines:
    first, last = (int(x) for x in line.split("-"))
    for x in range(first, last + 1):
        s = str(x)
        if len(s) % 2 == 0:
            fi = s[0:len(s)//2]
            se = s[len(s)//2:]
            if fi == se:
                result += x


# Part 1 = 30323879646
print(f"answer = {result}")

result = 0

for line in lines:
    first, last = (int(x) for x in line.split("-"))
    for x in range(first, last + 1):
        s = str(x)
        for i in range(1, len(s) // 2 + 1):
            v = s[:i]
            if s.replace(v, '') == '':
                result += x
                break

# Part 2 = 43872163557
print(f"answer = {result}")

# Second attempt without string replace
result = 0

for line in lines:
    first, last = (int(x) for x in line.split("-"))
    for x in range(first, last + 1):
        s = str(x)
        for i in range(1, len(s) // 2 + 1):
            v = s[:i]
            if len(s) % i != 0:
                continue
            j = i
            valid = True
            while j < len(s):
                if s[j:j+i] != v:
                    valid = False
                    break
                j += i
            if valid:
                result += x
                break

# Part 2 = 43872163557
print(f"answer = {result}")

import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

temp = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

lines = []
for t in temp:
    line = []
    for ch in t:
        line.append(int(ch))
    lines.append(line)

result = 0

for line in lines:
    mx = max(line[:-1])
    i = line.index(mx)
    my = max(line[i+1:])
    result += mx * 10 + my

# Part 1 = 17281
print(f"answer = {result}")


def recurse(line, e, ans):
    if e == 0:
        return
    a = len(line) - e + 1
    m = max(line[:a])
    i = line.index(m)
    ans.append(m)
    recurse(line[i+1:], e - 1, ans)


result = 0

for line in lines:
    ans = []
    recurse(line, 12, ans)
    result += int(("".join(str(x) for x in ans)))

# Part 2 = 171388730430281
print(f"answer = {result}")

# Do it without recursion.
result = 0

for line in lines:
    start = 0
    ans = []
    for i in range(11, -1, -1):
        a = len(line) - i
        m = max(line[start:a])
        start += line[start:].index(m) + 1
        ans.append(m)
    result += int(("".join(str(x) for x in ans)))


# Part 2 = 171388730430281
print(f"answer = {result}")

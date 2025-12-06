import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

# Insert leading whitespace to make part 2 cleaner.
lines = [" " + line for line in PUZZLE_INPUT.split("\n") if line]

cols = []
for line in lines:
    for i, x in enumerate(line.strip().split()):
        if len(cols) <= i:
            cols.append([x])
            continue
        cols[i].append(x)

result = 0

for col in cols:
    op = col.pop()
    ans = int(col.pop(0))
    for n in col:
        if op == "*":
            ans *= int(n)
        elif op == "+":
            ans += int(n)
        else:
            assert False
    result += ans


# Part 1 = 5667835681547
print(f"answer = {result}")

result = 0

operators = lines.pop().split()

col_num = 0
foo = []

for col_num in range(len(lines[0])):
    chars = []
    for line in lines:
        if line[~col_num] != " ":
            chars.append(line[~col_num])
    if chars:
        foo.append(int("".join(chars)))
    else:
        op = operators.pop()
        ans = foo.pop(0)
        for f in foo:
            if op == "*":
                ans *= f
            elif op == "+":
                ans += f
            else:
                assert False

        result += ans

        foo = []
    col_num += 1

# Part 2 = 9434900032651
print(f"answer = {result}")

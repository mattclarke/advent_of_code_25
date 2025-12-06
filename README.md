# advent_of_code_25
https://adventofcode.com/2025/

## Day 1
- Part 1: Use modulo to handle rotation.
- Part 2: First (working) attempt was brute force, i.e. rotate the dial one step at a time and count the zeroes. Works because the numbers are small but is inefficient.

Better solution: can divide the step size by 100 to get the number of complete rotations. Then the modulo can be used to check whether there is an extra pass through zero.
The gotcha is that when it is at zero from the previous move, do not count it moving negative as crossing zero. 

## Day 2
- Part 1: Split the string representation in half and compare the two parts
- Part 2: For each value, try every starting substring up to half the length (e.g. for 123456, try 1, 12, 123) and see if string replace all occurences leaves an empty string.

An alternative for part 2 which does not use string replace: again use a starting substring as before but compare it to each subsequent "chunk" to see if it repeats for the whole string.
```
input = 123123123
Try 1:
    Chunks are 1, 2, 3, 1, 2, 3, 1, 2, 3
    Does not match with second chunk (2)
Try 12:
    Chunks are 12, 31, 23, 12, 3
    Does not match with second chunk (31)
Try 123:
    Chunks are 123, 123, 123
    Matches
```

## Day 3
- Part 1: Find the first occurance of the highest number that isn't in the last position then find the highest value in the remaining sub-list.
- Part 2: Similar but using recursion. For the first value (a) it must be the highest value in the range `[0:-11]` because we need 12 values, the second value (b) must be the highest value in the range `[index of a + 1:-10]` and so on...

## Day 4
- Part 1: Put the bales/rolls in a set then count the neighbours for each one.
- Part 2: Reuse the code from part 1 but store the co-ordinates of the moveable bales and remove those from the set. Repeat until no more bales can be removed.

## Day 5
- Part 1: Simple nested loop to check if the items fit in any of the ranges.
- Part 2: First sort the ranges so that overlaps are easier to handle. Loop over the ranges while keeping track of the highest value seen (pos). If pos is less than the lower bound of the range add the whole range, if pos is greater than the lowest bound add the range from pos to the end of the range, or if pos is greater than the end of the range skip the whole range. 

## Day 5
- Part 1: Rearrange the data so all the data for each column is in it's own list with the operator at the end. Apply the operator to the rest of the list.
- Part 2: Remove the operator row and go through the original data starting from the right-most column. For each column collect the chars, create an int from them and store in a list. When a column is empty apply the corresponding operator to the list. Repeat until all columns done.

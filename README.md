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
- Part 2: Similar but using recursion. For the first value (a) it must be the highest value in the range `[0:-11]` because we need 12 values, the second value (b) must be the highest value in the range `[a.index() + 1:-10]` and so on... 

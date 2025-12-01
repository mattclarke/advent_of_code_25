# advent_of_code_25
https://adventofcode.com/2025/

## Day 1
- Part 1: Use modulo to handle rotation.
- Part 2: First (working) attempt was brute force, i.e. rotate the dial one step at a time and count the zeroes. Works because the numbers are small but is inefficient.

Better solution: can divide the step size by 100 to get the number of complete rotations. Then the modulo can be used to check whether there is an extra pass through zero.
The gotcha is that when it is at zero from the previous move, do not count it moving negative as crossing zero. 

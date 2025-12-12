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

## Day 6
- Part 1: Rearrange the data so all the data for each column is in it's own list with the operator at the end. Apply the operator to the rest of the list.
- Part 2: Remove the operator row and go through the original data starting from the right-most column. For each column collect the chars, create an int from them and store in a list. When a column is empty apply the corresponding operator to the list. Repeat until all columns done.

## Day 7
- Part 1: Follow each beam through each layer and count how many splits happen. Use a set for the beams to avoid duplicate splits.
- Part 2: Count the unique routes through, but DP on the splits otherwise it will take forever. The size of the DP dictionary is also the answer for part 1.

Internet solution: Pascal's triangle like, see code.

## Day 8
- Part 1: Calculate all the node to node distances and create a dict of distance to node pair. Sort the keys to get the 1000 shortest. For each distance connect the two nodes. Do a BFS for each node to calculate the number of connected nodes then pick the three longest circuits. To avoid duplication only allow visiting a node once.
- Part 2: Loop through all the connections starting from the shortest in a way similar to part 1 but for each connection add the two nodes to all nodes that connect to those two nodes. Continue until all 1000 nodes are connected in one circuit. Slow at ~80 seconds (Pypy).

Speed up: After connecting each pair, check to see if one of the pair connects to the other 1000 via a BFS. If it doesn't then continue connecting pairs. Takes ~3 seconds (Pypy).

Internet solution: Kruskal's algorithm, see code.

## Day 9
- Part 1: Loop through all the pairs and calculate the areas while tracking the maximum. To help with part 2, it keeps all the areas and corresponding tiles.
- Part 2: Tried a number of different ways which produced the same answer but the answer was wrong. After a lot of rewriting and debugging it turned out I made a mistake in the area calculation for part 1!!! The solution is quite simple: mark the rectangle invalid if either there are red tiles in the rectangle or the edge between two tiles crosses the rectangle. Start from the largest triangle and stop when the first rectangle passes.

## Day 10

## Day 11
- Part 1: BFS.
- Part 2: Number of routes explodes so simple BFS or DFS isn't an option. Use DP to find number of routes from 'svr' to 'fft', then 'fft' to 'dac' and, finally, 'dac' to 'out'. Multiple all of them together to get the total number of unique routes from 'svr' to 'out'. There were no routes from 'dac' to 'fft' so that made it simpler. I think because the graph is unidirectial this has to be the case.

Internet solution: cleaner implementation of DP, see code.

## Day 12:
- Part 1: Brute force takes about 120 seconds (Pypy).
- Part 2: No part 2 on the last day!

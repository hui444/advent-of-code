# [Day 1](https://adventofcode.com/2022/day/1) - Counting Calories

## Part 1: Get maximum calories:

Iterate through list once and store the maximum calorie between elves

- Time complexity: O(n)
- Space complexity: O(1)

## Part 2: Get sum of top 3 elf calories

Use max heap to keep track of calories between elves

- Time complexity: O(n lg n)
- Space complexity: O(n)

# [Day 2](https://adventofcode.com/2022/day/2) - Rock Paper Scissors

## Part 1: Get player's total score:

Iterate through the list, calculate the round score and sum the round scores to obtain total score

- Time complexity: O(n)
- Space complexity: O(1)

## Part 2: Get player's total score based on expected outcome:

Derive player's move based on opponent's move and expected outcome, compute points using part1 algo

- Time complexity: O(n)
- Space complexity: O(1)

# [Day 3](https://adventofcode.com/2022/day/3) - Rucksack Reorganization

## Part 1: Get rucksack item priority sum:

Iterate through the list, split each item into halves and find the common letters/'items' and sum the corresponding priority values

- Time complexity: O(n)
- Space complexity: O(1)

## Part 2: Get sum of badge priority:

Iterate through the list, find the common letters/'badges' of every 3 rows and sum the corresponding priority values

- Time complexity: O(n)
- Space complexity: O(1)

# [Day 4](https://adventofcode.com/2022/day/4) - Camp Cleanup

## Part 1: Get number of assignements that are fully contained:

Iterate through the list, get start and end of each range, check if they are fully contained within either ranges

- Time complexity: O(n)
- Space complexity: O(1)

## Part 2: Get number of overlapping assignments:

Iterate through the list, get start and end of each range.
Start of overlapping range: Max value between both start values
End of overlapping range: Min value between both end values
If the overlapping range is invalid (start > end), there is no overlap between the 2 ranges

- Time complexity: O(n)
- Space complexity: O(1)

# [Day 5](https://adventofcode.com/2022/day/5) - Supply Stacks

## Part 1: Get string of top crates after movement (using FIFO):

Parse input by splitting into:

1. Arrangements ("[H] [Z] [H] [H] [W] [S] [M]")
   1. Last row gives the number of stacks we have (" 1 2 3 4 5 6 7 8 9 ")
1. Movements ("move 15 from 2 to 4")
   And transforming arrangement into a dictionary of lists containing the crates, movements into a list of [number_of_stacks_to_move, source_stack, destination_stack]

Then, run the movement algorithm on the dictionary, each time taking the list of crates_to_move and reversing it to mimic FIFO before appending it to the destination_stack

- Time complexity: O(number of moves \* tallest stack height + tallest stack height \* number of stacks)
- Space complexity: O(number of crates + number of moves)

## Part 2: Get string of top crates after movement (by moving in batches):

Same as Part 1, but movement of crates are in batches, so we do not need to reverse the crates_to_move

- Time complexity: O(number of moves \* tallest stack height + tallest stack height \* number of stacks)
- Space complexity: O(number of crates + number of moves)

# [Day 6](https://adventofcode.com/2022/day/6) - Tuning Trouble

## Part 1: Get position of start of packet after marker (4 distinct characters):

Maintain a dictionary with the character as key and index as value. Update the dictionary for every character while checking if the letter exists in the dictionary and has an index >= start of marker. This means that we have to move the start of marker since the marker consists of 4 distinct characters.

Once the current index - start of marker index = 4, we found the start of packet

- Time complexity: O(length of string)
- Space complexity: O(1) - since we keep a dictionary of at most 26 alphabets

## Part 2: Get position of start of message after marker (14 distinct characters):

Same as Part 1, but number of distinct characters = 14 instead of 4

- Time complexity: O(length of string)
- Space complexity: O(1)

# [Day 7](https://adventofcode.com/2022/day/7) - No Space Left On Device

## Part 1: Get sum of directories with sizes <= 100000:

Get size of directory by maintaining a dictionary of absolute path as key and directory size as value and an list to keep track of the directories that we move into (eg [root, root/a, root/a/b] -> dir b is in dir a and dir root contains dir a and dir b)

1. command starts with `$ cd `
   1. next text is `..`: move out of directory
   1. next text is `/`: move to root directory
   1. else: move into new directory and add this to the list of directories we have
1. command starts with a digit -> size of a file in the directory
   since the file exists in the directory and all directories contained by the parent, we have to add this file size to the appropriate directory sizes
1. command starts with `$ ls` or `dir` -> ignore since it does not affect directory sizes

Get all sizes of directories in dictionary and sum the values <= 100000.

- Time complexity: O(number of lines \* number of directories)
- Space complexity: O(number of directories)

## Part 2: Get smallest directory size to delete to free up device for update:

Get dictionary sizes and iterate through the sizes to find the smallest size directory that is >= size to free up to update device.

- Time complexity: O(number of lines \* number of directories)
- Space complexity: O(number of directories)

# [Day 8](https://adventofcode.com/2022/day/8) - Treetop Tree House

## Part 1: Get number of trees visible from edge of forest:

For each tree in forest, iterate through the directions to see if it is visible from the edge and count it if it is visible. The tree is visible if there exist no tree with height greater than itself.

- Time complexity: O(number of trees \* max(number of row, number of columns))
- Space complexity: O(1)

## Part 2: Get maximum scenic score of trees in the forest:

For each tree in forest, iterate through the directions and count the number of trees in view and calculate the scenic score. A tree is in view if there exist no tree between it and the view point tree that is taller than the view point tree height. From the tree's scenic score, we can keep track of the maximum scenic score of the trees in the forest

- Time complexity: O(number of trees \* max(number of row, number of columns))
- Space complexity: O(1)

# [Day 9](https://adventofcode.com/2022/day/9) - Rope Bridge

## Part 1: Get number of distinct positions visited by tail knot:

Move head knot based on instructions and move tail knot to fulfill the conditions. Then add the new tail knot position into the visited set to find the number of distinct positions visited.

To find the new position of the tail knot, we find the distance between itself and the head knot and shift the x and y coordinate by at most 1 towards the head knot coordinate.

- Time complexity: O(number of moves by head knot)
- Space complexity: O(number of positions visited by tail knot)

## Part 2: Get number of distinct positions visited by last knot in rope (knot 9):

Move head knot based on instructions and move the subsequent knots based on its preceeding knot, to fulfill the conditions. Then add the new knot 9 position into the visited set to find the number of distinct positions visited.

- Time complexity: O(number of moves by head knot)
- Space complexity: O(number of positions visited by last knot)

# [Day 10](https://adventofcode.com/2022/day/10) - Cathode Ray Tube

## Part 1: Get sum of signal strength during specific cycles:

For "noop" operations, we increment the number of cycles and update the X value. For "addx V" operations, we will increment the number of cycles by 2 and only update the value of X during the second cycle. While updating X, when the number of cycles correspond to 20, 60, 100, 140, 180 or 220, we will calculate the signal strength and update the sum accordingly.

- Time complexity: O(n)
- Space complexity: O(1)

## Part 2: Get letters displayed on CRT:

Maintain CRT window starting point, the x coordinate of the pixel can be derived from `(num_cycle - 1) // CRT_WIDTH` and the y coordinate from `(num_cycle - 1) % CRT_WIDTH`. And we can get the pixel based on whether the pixel is in the CRT window. Each cycle updates the CRT window based on X.

- Time complexity: O(n)
- Space complexity: O(1) - space required is constant since CRT will always be 40 by 6

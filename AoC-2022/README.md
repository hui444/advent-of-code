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

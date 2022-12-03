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

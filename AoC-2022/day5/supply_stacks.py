from collections import defaultdict, deque 

f = open("day5/input.txt", "r")
f = f.read().split("\n")

def get_num_stacks(stacks_row): # O(1)
    return len(stacks_row.split())

def parser(): # O(number of moves + tallest stack height * number of stacks)
    isMovement = False
    arrangement = []
    movement = []
    for row in f: # O(number of moves + tallest stack height)
        if not isMovement and row == '':
            isMovement = True
            continue 
        if isMovement:
            movement.append(row)
        else:
            arrangement.append(row)
    stacks_row = arrangement[-1]
    arrangement = arrangement[:-1]
    num_stacks = get_num_stacks(stacks_row)

    stacks = defaultdict(list, { k: [] for k in range(1, num_stacks + 1) })

    for level in range(len(arrangement) - 1, -1, -1): # O(tallest stack height)
        row = arrangement[level]
        position = 0
        num_spaces = 0
        while position < len(row): # O(number of stacks)
            index = position + num_spaces
            crate = row[index:index+3].strip()
            if crate:
                stacks[position // 3 + 1].append(row[index + 1])
            num_spaces += 1
            position += 3

    moves = []
    for move in movement: # O(number of moves)
        num_crates, move = move.split(" from ")
        num_crates = num_crates[5:]
        from_stack, to_stack = move.split(" to ")
        moves.append([int(num_crates), int(from_stack), int(to_stack)])
    return [moves, stacks]

def move_crates(moves, stacks, isFIFO=False): # O(number of moves * tallest stack height)
    for move in moves: # O(number of moves)
        num_crates, from_stack, to_stack = move
        crates_to_move = stacks[from_stack][-num_crates:]
        if isFIFO:
            crates_to_move.reverse()  # O(tallest stack height)
        stacks[to_stack] += crates_to_move
        stacks[from_stack] = stacks[from_stack][:-num_crates]
    return stacks

def get_top_crate_string(stacks): # O(number of stacks)
    top_crates_string = ""
    for i in range(1, len(stacks) + 1):
        if len(stacks[i]):
            top_crates_string += stacks[i][-1]

    return top_crates_string

def get_top_crate_after_singular_movements(): # O(number of moves * tallest stack height + tallest stack height * number of stacks)
    moves, stacks = parser() 
    move_crates(moves, stacks, True) 
    return get_top_crate_string(stacks) 
    
print(f"part1: {get_top_crate_after_singular_movements()}")

def get_top_crate_after_batch_movements():
    moves, stacks = parser()
    move_crates(moves, stacks)
    return get_top_crate_string(stacks)

print(f"part2: {get_top_crate_after_batch_movements()}")

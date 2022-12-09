f = open("day9/input.txt", "r")
f = f.read().split("\n")
    
NUMBER_OF_KNOTS = 9

def get_new_t_position(t_position, h_position): # O(1)
    x_diff = h_position[0] - t_position[0]
    y_diff = h_position[1] - t_position[1]
    if (abs(x_diff) > 1 or abs(y_diff) > 1):
        x_delta = 0
        if x_diff > 0:
            x_delta = 1
        elif x_diff < 0:
            x_delta = -1

        y_delta = 0
        if y_diff > 0:
            y_delta = 1
        elif y_diff < 0:
            y_delta = -1

        t_position = (t_position[0] + x_delta, t_position[1] + y_delta)

    return t_position

def get_new_h_position(h_position, direction): # O(1)
    x_delta = y_delta = 0

    if direction == "U":
        x_delta = -1
    elif direction == "D":
        x_delta = 1
    elif direction == "L":
        y_delta = -1
    elif direction == "R":
        y_delta = 1

    return (h_position[0] + x_delta, h_position[1] + y_delta)

def get_num_distinct_tail_positions(): # O(number of moves by head knot)
    visited_positions = set()
    t_position = h_position = (0, 0)
    for instruction in f:
        direction, count = instruction.split(" ")
        count = int(count)
        while count:
            count -= 1
            h_position = get_new_h_position(h_position, direction)
            t_position = get_new_t_position(t_position, h_position)
            visited_positions.add(t_position)

    return len(visited_positions)

print(f"part1: {get_num_distinct_tail_positions()}")

def get_distinct_knots_positions():
    visited_positions = set()
    h_position = (0, 0)
    t_positions = [(0, 0) for _ in range(NUMBER_OF_KNOTS)]

    for instruction in f:
        direction, count = instruction.split(" ")
        count = int(count)

        while count: 
            count -= 1
            h_position = get_new_h_position(h_position, direction)
            t_positions[0] = get_new_t_position(t_positions[0], h_position)

            for i in range(1, NUMBER_OF_KNOTS): # O(1)
                t_positions[i] = get_new_t_position(t_positions[i], t_positions[i - 1])

            visited_positions.add(t_positions[-1])

    return len(visited_positions)

print(f"part2: {get_distinct_knots_positions()}")

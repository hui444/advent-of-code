f = open("day10/input.txt", "r")
f = f.read().split("\n")

ADD = "addx" # 2 cycles to complete
NOOP = "noop" # 1 cycle to complete
SINAL_STRENGTH_INDICATOR_CYCLES = [20, 60, 100, 140, 180, 220]

def get_signal_strength(num_cycle, X):
    signal_strength = 0
    if num_cycle in SINAL_STRENGTH_INDICATOR_CYCLES:
            signal_strength += num_cycle * X
    return signal_strength

def get_signal_strength_sum(): # O(n)
    num_cycle = 0
    X = 1
    signal_strength_sum = 0
    for instruction in f:
        num_cycle += 1
        # start cycle
        signal_strength_sum += get_signal_strength(num_cycle, X)
        if instruction == NOOP:
            continue
        # end cycle
        num_cycle += 1
        # start cycle
        signal_strength_sum += get_signal_strength(num_cycle, X)
        V = int(instruction[len(ADD) + 1:])
        X += V
        # end cycle

    return signal_strength_sum

print(f"part1: {get_signal_strength_sum()}")

CRT_WIDTH = 40
CRT_HEIGHT = 6
LIT_PIXEL = "#"
DARK_PIXEL = "."

def print_CRT(CRT_data): # O(1) 
    CRT = ""
    for row in CRT_data:
        for col in row:
            CRT += col 
        CRT += "\n"
    print(CRT)

def get_pixel_position(num_cycle):
    position = (num_cycle - 1)
    return (position // CRT_WIDTH, position % CRT_WIDTH)

def get_pixel(num_cycle, sprite_start_position):
    pixel = DARK_PIXEL
    pixel_x_position = num_cycle % 40 - 1
    if pixel_x_position in [sprite_start_position + i for i in range(3)]:
        pixel = LIT_PIXEL

    return pixel

def draw_CRT():
    CRT_data = [[DARK_PIXEL for _ in range(CRT_WIDTH)] for _ in range(CRT_HEIGHT)] # O(1) 
    X = 1
    num_cycle = 0

    for instruction in f:  # O(n) 
        num_cycle += 1
        # start cycle
        x, y = get_pixel_position(num_cycle)
        CRT_data[x][y] = get_pixel(num_cycle, X - 1)
        if instruction == NOOP:
            continue
        # end cycle

        num_cycle += 1
        # start cycle
        x, y = get_pixel_position(num_cycle)
        CRT_data[x][y] = get_pixel(num_cycle, X - 1)
        V = int(instruction[len(ADD) + 1:])
        X += V
        # end cycle

    print_CRT(CRT_data)

print("part2: ")
draw_CRT()
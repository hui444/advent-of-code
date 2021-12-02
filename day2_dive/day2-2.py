input_list = []

f = open("input.txt", "r")
input_list = f.read().split("\n")

horizontal_position = 0
depth = 0
aim = 0

for input in input_list:
    command = input.split(' ')[0]
    value = (int)(input.split(' ')[1])
    if command == "forward":
        horizontal_position += value
        depth += aim * value
    elif command == 'down':
        aim += value
    elif command == 'up':
        aim -= value
    else:
        print('unknown command: ', input)

print('horizontal position: %d, depth: %d' % (horizontal_position, depth))

final_value = horizontal_position * depth

print('final value %d' % final_value)
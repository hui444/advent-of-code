f = open("day7/input.txt", "r")
f = f.read().split("\n")

CHANGE_DIRECTOR_STARTING_COMMAND = "$ cd "
CD_MOVE_OUT = ".."
CD_SWITCH_OUT_DIR = "/"
MAX_DIR_SIZE = 100000
ROOT_DIR = "root"

MAX_FILE_SYSTEM_SIZE = 70000000
FREE_SPACE_TO_UPDATE = 30000000

def get_directory_sizes(): # O(number of lines * number of directories)
    dir_size_dict = dict({ROOT_DIR: 0})
    current_dir = [ROOT_DIR]
    for command in f: # O(number of lines)
        if command.startswith(CHANGE_DIRECTOR_STARTING_COMMAND):
            instruction = command[len(CHANGE_DIRECTOR_STARTING_COMMAND):]
            if instruction == CD_SWITCH_OUT_DIR:
                current_dir = [ROOT_DIR]
            elif instruction == CD_MOVE_OUT:
                current_dir.pop()
            else:
                new_dir = "/".join([current_dir[-1], instruction])
                current_dir.append(new_dir)
                dir_size_dict[new_dir] = 0
        if command[0].isdigit():
            for dir in current_dir: # O(number of directories)
                file_size = int(command.split(" ")[0])
                dir_size_dict[dir] += file_size

    return dir_size_dict

def get_total_size_of_directories(): # O(number of lines * number of directories)
    dir_size_dict = get_directory_sizes() # O(number of lines * number of directories)
    dir_sizes = dir_size_dict.values()

    sum_dir_sizes = 0
    for size in dir_sizes: # O(number of directories)
        if size <= MAX_DIR_SIZE:
            sum_dir_sizes += size
    
    return sum_dir_sizes

print(f"part1: {get_total_size_of_directories()}")

def get_smallest_dir_to_delete_to_update():
    dir_size_dict = get_directory_sizes() # O(number of lines * number of directories)
    unused_space = MAX_FILE_SYSTEM_SIZE - dir_size_dict[ROOT_DIR]
    min_space_needed = FREE_SPACE_TO_UPDATE - unused_space
    dir_sizes = dir_size_dict.values()
    min_dir_size_to_delete = MAX_FILE_SYSTEM_SIZE

    for size in dir_sizes: # O(number of directories)
        if size >= min_space_needed:
            min_dir_size_to_delete = min(min_dir_size_to_delete, size)

    return min_dir_size_to_delete

print(f"part2: {get_smallest_dir_to_delete_to_update()}")

from collections import defaultdict

input_list = []

f = open("input.txt", "r")
input_list = f.read().split("\n")
coordinates_list = []

for i in range(len(input_list)):
    coordinates = input_list[i].split(' -> ')
    init_coordinate = coordinates[0].split(',')
    init_x = int(init_coordinate[0])
    init_y = int(init_coordinate[1])
    final_coordinate = coordinates[1].split(',')
    diff_x = int(final_coordinate[0]) - init_x
    diff_y = int(final_coordinate[1]) - init_y

    coordinates_list.append([
        [init_x, init_y],
        [diff_x, diff_y]
    ])

# Initialize dictionary
marked_coordinates = defaultdict(int)
    
def updateCoordinateLists(coordinate):
    marked_coordinates[str(coordinate)] += 1
    
def addCoordinatesToList(coordinates, ignore_diagonals):
    init_coordinate = coordinates[0]
    init_x = init_coordinate[0]
    init_y = init_coordinate[1]
    movement_coordinate = coordinates[1]
    movement_x = movement_coordinate[0]
    movement_y = movement_coordinate[1]
    # diagonal lines
    if movement_x != 0 and movement_y != 0:
        if ignore_diagonals:
            return
        else:
            for i in range(abs(movement_x) + 1):
                # m_x > 0
                if movement_x > 0:
                    # m_y > 0
                    x_value = init_x + i
                    if movement_y > 0:
                        y_value = init_y + i
                    # m_y < 0
                    else:
                        y_value = init_y - i
                # m_x < 0
                else:
                    x_value = init_x - i
                    # m_y > 0
                    if movement_y > 0:
                        y_value = init_y + i
                    # m_y < 0
                    else:
                        y_value = init_y - i
                coordinate = [x_value, y_value]
                updateCoordinateLists(coordinate)
            return

    if movement_x != 0:
        for i in range(abs(movement_x) + 1):
            if movement_x < 0:
                x_value = init_x + movement_x + i
            else:
                x_value = init_x + i
            coordinate = [x_value, init_y]
            updateCoordinateLists(coordinate)
    elif movement_y != 0:
        for i in range(abs(movement_y) + 1):
            if movement_y < 0:
                y_value = init_y + movement_y + i
            else:
                y_value = init_y + i
            coordinate = [init_x, y_value]
            updateCoordinateLists(coordinate)

def intercepts_of_vertical_horizontal_lines():
    duplicated_coordinates = 0
    for i in range(len(coordinates_list)):
        addCoordinatesToList(coordinates_list[i], True)
    for j in marked_coordinates:
        if marked_coordinates[j] >= 2:
            duplicated_coordinates += 1
    return duplicated_coordinates

part1 = intercepts_of_vertical_horizontal_lines()
print("part1: ", part1)

def intercepts_of_all_lines():
    duplicated_coordinates = 0
    for i in range(len(coordinates_list)):
        addCoordinatesToList(coordinates_list[i], False)
    for j in marked_coordinates:
        if marked_coordinates[j] >= 2:
            duplicated_coordinates += 1
    return duplicated_coordinates

marked_coordinates = defaultdict(int)
part2 = intercepts_of_all_lines()
print("part2: ", part2)
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

marked_coordinates = []
duplicated_coordinates = []
    
def updateCoordinateLists(coordinate):
    if coordinate in marked_coordinates and coordinate not in duplicated_coordinates:
        duplicated_coordinates.append(coordinate)
    else:
        marked_coordinates.append(coordinate)
    
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
            print(movement_x, movement_y)
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

# def part1():
#     for i in range(len(coordinates_list)):
#         addCoordinatesToList(coordinates_list[i], True)
#     print(len(duplicated_coordinates))

# part1()

def part2():
    for i in range(len(coordinates_list)):
        addCoordinatesToList(coordinates_list[i], False)
        print(i, len(coordinates_list))
    print(len(duplicated_coordinates))

part2()
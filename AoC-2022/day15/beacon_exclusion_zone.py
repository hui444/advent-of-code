import re

f = open("day15/input.txt", "r")
f = f.read().split("\n")

SENSOR_X_TEXT = "Sensor at x="
SENSOR_Y_TEXT = ", y="
CLOSEST_BEACON_X_TEXT = ": closest beacon is at x="
CLOSEST_BEACON_Y_TEXT = ", y="

def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def parser():
    data = []
    for line in f:
        line = (line[len(SENSOR_X_TEXT):]).split(CLOSEST_BEACON_X_TEXT)
        sensor_coordinates = sensor_x, sensor_y = [int(val) for val in line[0].split(SENSOR_Y_TEXT)]
        beacon_coordinates = [int(val) for val in line[1].split(CLOSEST_BEACON_Y_TEXT)]
        data.append((sensor_x, sensor_y, get_distance(sensor_coordinates, beacon_coordinates)))
    return data

LINE = 4000000 // 2

def get_sorted_line_intervals(data): 
    intervals = []
    for x, y, dist in data:
        for d in [dist - abs(LINE - y)]:
            if d >= 0:
                intervals.append((x - d, x + d))
    return sorted(intervals)

def get_num_positions_with_no_beacons():
    data = parser()
    intervals = get_sorted_line_intervals(data)
    start, stop, holes = *intervals[0], 0

    for nstart, nstop in intervals: 
        holes, stop = max(0, nstart-stop-1), max(stop, nstop)

    return stop - start - holes

print(f"part1: {get_num_positions_with_no_beacons()}")

def tuning_frequency():
    data = parser()
    a = set(x-y+r+1 for x,y,r in data).intersection(x-y-r-1 for x,y,r in data).pop()
    b = set(x+y+r+1 for x,y,r in data).intersection(x+y-r-1 for x,y,r in data).pop()

    return (a + b) * LINE + (b - a) // 2

print(f"part2: {tuning_frequency()}")
from enum import Enum

f = open("day17/input.txt", "r")
movements = f.read().split()

ROCK1 = "####"
ROCK2 = ".#.\n###\n.#."
ROCK3 = "..#\n..#\n###"
ROCK4 = "#\n#\n#\n#"
ROCK5 = "##\n##"

ROCKS = [ROCK1, ROCK2, ROCK3, ROCK4, ROCK5]

def get_height_of_rocks_tower(number_of_fallen_rocks):
    for i in range(number_of_fallen_rocks):
        rock = ROCKS[i % 6]
        
    pass


print(f"part1: {get_height_of_rocks_tower(2022)}")
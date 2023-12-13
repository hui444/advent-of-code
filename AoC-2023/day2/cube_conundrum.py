# https://adventofcode.com/2023/day/2

from math import prod
from utils.read_input import read_input
from utils.print_answer import print_answer

cube_color_to_number = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_possible_game(game_sets):
    for game in game_sets:
        for cubes in game.split(", "):
            game_color_to_number = cube_color_to_number.copy()
            [num_cubes, color] = cubes.split(" ")
            game_color_to_number[color] -= int(num_cubes)

            if game_color_to_number[color] < 0:
                return False

    return True

def sum_of_possible_game_ids(document_text):
    ids_sum = 0
    for game_text in document_text:
        [game_id, game_sets] = game_text.split(": ")
        game_id = int(game_id[5:])
        game_sets = game_sets.split("; ")
        if is_possible_game(game_sets):
            ids_sum += game_id

    return ids_sum    

game_document_text = read_input('/AoC-2023/day2/input.txt').split('\n')

print_answer(1, sum_of_possible_game_ids(game_document_text))

def get_power_of_game(game_sets):
    cube_color_to_number_dict = {
        "red": 0,
        "green": 0,
        "blue": 0
    } 
    for game in game_sets:
        for cubes in game.split(", "):
            [num_cubes, color] = cubes.split(" ")
            cube_color_to_number_dict[color] = max(cube_color_to_number_dict[color], int(num_cubes))

    return prod(cube_color_to_number_dict.values())

def sum_of_power_of_game_sets(document_text):

    sum_of_power = 0
    for game_text in document_text:
        [game_id, game_sets] = game_text.split(": ")
        game_id = int(game_id[5:])
        game_sets = game_sets.split("; ")
        
        sum_of_power += get_power_of_game(game_sets)

    return sum_of_power    

print_answer(2, sum_of_power_of_game_sets(game_document_text))
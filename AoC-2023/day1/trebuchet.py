# https://adventofcode.com/2023/day/1

from utils.read_input import read_input
from utils.print_answer import print_answer

def get_calibration_value_sum(document_text):
    sum = 0
    for text in document_text:
        number = ""
        for char in text:
            if char.isnumeric():
                number += char
        sum += int(number[0] + number[-1])

    return sum

calibration_document_text = read_input('/AoC-2023/day1/input.txt').split('\n')

print_answer(1, get_calibration_value_sum(calibration_document_text))

number_texts = ["one", "two", "three",  "four", "five", "six", "seven", "eight", "nine"]

def get_new_calibration_value_sum(document_text):
    sum = 0
    for text in document_text:
        number = ""
        for i in range(len(text)):
            char = text[i]
            if char.isnumeric():
                number += char
            else: 
                # check if text contains number
                for j in range(len(number_texts)):
                    if text.startswith(number_texts[j], i):
                        number += str(j + 1)
        sum += int(number[0] + number[-1])
    return sum

print_answer(2, get_new_calibration_value_sum(calibration_document_text))

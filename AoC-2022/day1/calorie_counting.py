from heapq import heappush, heapify

f = open("day1/input.txt", "r")
f = f.read().split("\n")

def get_max_calories():
    max_calorie = 0
    elf_calorie = 0

    for item in f:
        if item == "":
            max_calorie = max(max_calorie, elf_calorie)
            elf_calorie = 0
        else:
            elf_calorie += int(item)
    return max_calorie

print(f"part1: {get_max_calories()}")

def get_top3_calorie_sum():
    elf_calorie = 0
    max_heap = []
    heapify(max_heap)

    for item in f:
        if item == "":
            heappush(max_heap, -1 * elf_calorie)
            elf_calorie = 0
        else:
            elf_calorie += int(item)
    
    return -1 * sum(max_heap[:3])
    
print(f"part2: {get_top3_calorie_sum()}")

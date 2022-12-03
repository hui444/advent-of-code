f = open("day3/input.txt", "r")
f = f.read().split("\n")

def get_common_items_list(*args):
    common_items = set(args[0])
    args = args[1:]
    for arg in args:
        common_items &= set(arg)
    return list(common_items)

def get_priority(item):
    item_ord = ord(item)
    if item_ord >= ord('a') and item_ord <= ord('z'):
        return item_ord - 96
    return item_ord - 38

def get_item_priorities_sum():
    common_items = []
    for rucksack in f:
        rucksack1 = rucksack[:len(rucksack) // 2]
        rucksack2 = rucksack[len(rucksack) // 2:]
        common_items += get_common_items_list(rucksack1, rucksack2)

    priorities_sum = 0
    for item in common_items:
        priorities_sum += get_priority(item)

    return priorities_sum
        
print(f"part1: {get_item_priorities_sum()}")

def get_badge_priorities_sum():
    badges = []
    i = 0
    while i + 2 < len(f):
        rucksack1, rucksack2, rucksack3 = f[i], f[i + 1], f[i + 2]
        badges += get_common_items_list(rucksack1, rucksack2, rucksack3)
        i += 3

    priorities_sum = 0
    for badge in badges:
        priorities_sum += get_priority(badge)

    return priorities_sum

print(f"part2: {get_badge_priorities_sum()}")

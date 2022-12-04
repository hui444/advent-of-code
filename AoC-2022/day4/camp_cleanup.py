f = open("day4/input.txt", "r")
f = f.read().split("\n")

def is_fully_contained(range1, range2):
    r1_start, r1_end = [int(i) for i in range1.split("-")]
    r2_start, r2_end = [int(i) for i in range2.split("-")]

    # r2 contained in r1
    if r1_start <= r2_start and r2_end <= r1_end:
        return True
    # r1 contained in r2
    if r2_start <= r1_start and r1_end <= r2_end:
        return True
    
    return False

def get_num_pairs_fully_contained():
    num_pairs = 0
    for section_pair in f:
        section1, section2 = section_pair.split(",")
        if is_fully_contained(section1, section2):
            num_pairs += 1
    return num_pairs

print(f"part1: {get_num_pairs_fully_contained()}")

def get_overlapping_section_range(range1, range2):
    r1_start, r1_end = [int(i) for i in range1.split("-")]
    r2_start, r2_end = [int(i) for i in range2.split("-")]

    start = max(r1_start, r2_start)
    end = min(r1_end, r2_end)

    return start <= end

def get_num_overlapping_sections():
    num_overlapping_sections = 0
    for section_pair in f:
        section1, section2 = section_pair.split(",")
        if get_overlapping_section_range(section1, section2):
            num_overlapping_sections += 1
    return num_overlapping_sections

print(f"part2: {get_num_overlapping_sections()}")
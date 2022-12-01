input_list = []

f = open("input.txt", "r")
input_list = f.read().split(",")
input_list = list(map(int, input_list))

print("Enter number of days elapsed:")

days_elapsed = int(input())
max_fish_age = 8

# update fishes_list => format {0: 1, ...} = {fish_age: number_of_fishes, ...}
# move number of fishes down everyday, add reproduced fish to age 8 and age 6
def update_fishes_list(raw_fishes_list):
    new_fishes_list = dict.fromkeys(range(max_fish_age + 1), 0)
    for fish_age in range(max_fish_age + 1):
        new_fishes_list[fish_age] = raw_fishes_list[(fish_age + 1) % 9] 
        if fish_age == 6:
            new_fishes_list[fish_age] += raw_fishes_list[0]
    return new_fishes_list

fishes_list = dict.fromkeys(range(max_fish_age + 1), 0)
# initialise fishes_list with input
for i in range(len(input_list)):
    fishes_list[input_list[i]] += 1

for i in range(days_elapsed):
    fishes_list = update_fishes_list(fishes_list)

number_of_fishes = sum(fishes_list.values())

print("Number of fishes after %d days: %d" % (days_elapsed, number_of_fishes))


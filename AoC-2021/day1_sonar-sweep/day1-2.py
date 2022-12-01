input_list = []

f = open("input.txt", "r")
f = f.read().split("\n")
input_list = [int(i) for i in f]

input_list = list(map(int, input_list))

count = 0
for i in range(len(input_list)-3):
    first_window = input_list[i] + input_list[i+1] + input_list[i+2]
    second_window = input_list[i+1] + input_list[i+2] + input_list[i+3]

    if first_window < second_window:
        count += 1

print(count)
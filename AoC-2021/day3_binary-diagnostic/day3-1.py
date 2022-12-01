input_list = []

f = open("input.txt", "r")
input_list = f.read().split("\n")
numOfDigits = len(input_list[0])

gamma_rate = [0] * numOfDigits
epsilon_rate = [0] * numOfDigits

def binaryToDecimal(n):
    return int(n,2)

def joinIntToString(list):
    string_ints = [str(int) for int in list]
    return binaryToDecimal(''.join(string_ints))

for i in range(numOfDigits):
    zeros = 0
    ones = 0
    for j in range(len(input_list)):
        digit = int(input_list[j][i])
        if digit == 0:
            zeros += 1
        elif digit == 1:
            ones += 1
    if zeros > ones:
        gamma_rate[i] = 0
        epsilon_rate[i] = 1
    elif ones > zeros:
        gamma_rate[i] = 1
        epsilon_rate[i] = 0

gamma_rate = joinIntToString(gamma_rate)
epsilon_rate = joinIntToString(epsilon_rate)

power_consumption = gamma_rate * epsilon_rate

print("power consumption: %d" % power_consumption)
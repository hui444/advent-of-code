input_list = []

f = open("input.txt", "r")
input_list = f.read().split("\n")

def binaryToDecimal(n):
    return int(n,2)

def reduceList(values, tiebreaker):
    for i in range(len(values[0])):
        zeros = 0
        ones = 0
        for j in range(len(values)):
            digit = int(values[j][i])
            if digit == 0:
                zeros += 1
            elif digit == 1:
                ones += 1
        if zeros > ones:
            values = list(filter(lambda val: int(val[i]) == 1-tiebreaker, values))
        else:
            values = list(filter(lambda val: int(val[i]) == tiebreaker, values))
        if len(values) == 1:
            return binaryToDecimal(values[0])

c02_generator_rating = reduceList(input_list, 0)
oxygen_generator_rating = reduceList(input_list, 1)

life_support_rating = c02_generator_rating * oxygen_generator_rating

print("c02 generator rating: %d" % c02_generator_rating)
print("oxygen generator rating: %d" % oxygen_generator_rating)
print("life support rating: %d" % life_support_rating)
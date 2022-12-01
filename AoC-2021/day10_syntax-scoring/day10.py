syntax_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

closing_char = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

opening_char = dict((v,k) for k,v in closing_char.items())

opening_string = "([{<"
closing_string = ")]}>"

input_list = []

f = open("input.txt", "r")
input_list = f.read().split("\n")

def findFirstCorruptedChar(chunk):
    stack = []
    for i in range(len(chunk)):
        char = chunk[i]
        if char in opening_string:
            stack.append(char)
        else:
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == '>' and stack[-1] == '<':
                stack.pop()
            else:
                # corrupted char
                return char

def calculateSyntaxErrorScore(corrupted_string):
    score = 0
    for i in range(len(corrupted_string)):
        corrupted_char = corrupted_string[i]
        score += syntax_points[corrupted_char]
    return score

def findSyntaxErrorScore(navigation_subsystem):
    corrupted_list = []

    for i in range(len(navigation_subsystem)):
        corrupted_char = findFirstCorruptedChar(navigation_subsystem[i])
        if corrupted_char: 
            corrupted_list.append(corrupted_char)
    
    score = calculateSyntaxErrorScore(corrupted_list)
    return score
    
part1 = findSyntaxErrorScore(input_list)
print("part 1: %s" % part1)

def findIncompleteString(chunk):
    stack = []
    for i in range(len(chunk)):
        char = chunk[i]
        if char in opening_string:
            stack.append(char)
        else:
            if char in closing_string and stack[-1] == opening_char[char]:
                stack.pop()
            else:
                # corrupted char
                return None
    return stack

def getMissingStringScore(stack):
    score = 0
    for i in range(len(stack)):
        last_char = stack[-1]
        stack.pop()
        score = (score * 5) + autocomplete_points[closing_char[last_char]]
    return score

def findAutocompleteScore(navigation_subsystem):
    score_list = []
    for i in range(len(navigation_subsystem)):
        incomplete_string = findIncompleteString(navigation_subsystem[i])
        if incomplete_string:
            print(incomplete_string)
            score_list.append(getMissingStringScore(incomplete_string))
    score_list.sort()
    return score_list[int(len(score_list)/2)]

part2 = findAutocompleteScore(input_list)
print("part 2: %s" % part2)

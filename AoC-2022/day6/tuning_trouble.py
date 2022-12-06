text = open("day6/input.txt", "r")
text = text.read()

START_OF_PACKET_MARKER_LENGTH = 4
START_OF_MESSAGE_MARKER_LENGTH = 14

def get_num_char_to_start_text_after_marker(marker_length):
    start = 0
    char_dict = {}

    for i in range(len(text)): # O(length of text)
        letter = text[i]
        prev_char_occurence = char_dict.get(letter)

        if i - start == marker_length:
            break
        
        if prev_char_occurence != None and prev_char_occurence >= start:
            start = prev_char_occurence + 1
        char_dict[letter] = i

    return start + marker_length

print(f"part1: {get_num_char_to_start_text_after_marker(START_OF_PACKET_MARKER_LENGTH)}")
print(f"part2: {get_num_char_to_start_text_after_marker(START_OF_MESSAGE_MARKER_LENGTH)}")


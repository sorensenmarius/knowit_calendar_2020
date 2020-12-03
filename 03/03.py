import numpy as np
import requests

m = requests.get('https://gist.githubusercontent.com/knowitkodekalender/d277d4f01a9fe10f7c1d92e2d17f1b31/raw/49da54e4372a83f4fc11d7137f19fc8b4c58bda6/matrix.txt').content.decode().split('\n')
words = requests.get('https://gist.githubusercontent.com/knowitkodekalender/9e1ba20cd879b0c6d7af4ccfe8a87a19/raw/b19ae9548a33a825e2275d0283986070b9b7a126/wordlist.txt').content.decode().split("\n")

directions = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
not_found_words = []

def check_next_letter(current_position, word, index, d):
    if index == len(word):
        return True

    new_pos = [current_position[0] + d[0], current_position[1] + d[1]]

    if -1 in new_pos or 1000 in new_pos:
        return False

    if word[index] == m[new_pos[0]][new_pos[1]]:
        return check_next_letter(new_pos, word, index + 1, d)
    return False

for word in words:
    word_found = False
    starting_positions = []
    for row_number, row in enumerate(m):
        char_indexes = [pos for pos, char in enumerate(row) if char == word[0]]

        for char_index in char_indexes:
            starting_positions.append([row_number, char_index])

    for pos in starting_positions:
        for direction in directions:
            if check_next_letter(pos, word, 1, direction):
                word_found = True
                break
    
    if not word_found:
        not_found_words.append(word)

print(not_found_words)
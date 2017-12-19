#!/usr/bin/python3

import sys

x_moves = [1, 0, -1, 0]
y_moves = [0, -1, 0, 1]

def peek_move(x, y, direction):
    peek_x = x + x_moves[direction]
    peek_y = y + y_moves[direction]
    if peek_y < 0 or peek_y >= len(grid):
        return False, None, None, None

    row = grid[peek_y]
    if peek_x < 0 or peek_x >= len(row):
        return False, None, None, None

    peek_char = row[peek_x]
    if peek_char == ' ':
        return False, None, None, None

    return True, peek_x, peek_y, peek_char

with open(sys.argv[1]) as input_file:
    grid = [list(l.rstrip()) for l in input_file]

# Find start location
y = 0
x = grid[0].index('|')

# Initially going down
direction = 3

letters = ''
moves = 1
while True:
    found_move = False
    for d in (direction, (direction + 1) % 4, (direction - 1) % 4):
        can_move, next_x, next_y, next_char = peek_move(x, y, d)
        if can_move:
            x, y, direction = next_x, next_y, d
            moves += 1
            found_move = True
            if str.isalpha(next_char):
                letters += next_char
            break

    if not found_move:
        break

print(letters, moves)

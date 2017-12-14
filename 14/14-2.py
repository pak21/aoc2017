#!/usr/bin/python3

import collections
import sys

def round(string, position, skip, lengths):
    for length in lengths:
        new_string = string[:]
        for i in range(0, length):
            new_string[(position + length - 1 - i) % total_length] = string[(position + i) % total_length]
        string = new_string

        position += length + skip
        skip += 1

    return string, position, skip

def knot_hash(input_string):
    lengths = [ord(c) for c in input_string]
    lengths.extend([17, 31, 73, 47, 23])

    string = list(range(0, total_length))
    position = 0
    skip = 0

    for i in range(0, 64):
        string, position, skip = round(string, position, skip, lengths)

    output = []
    for i in range(0, 16):
        checksum = 0
        for j in range(0, 16):
            checksum ^= string[16 * i + j]
        output.append(checksum)

    return output

def int_to_bits(i):
    return [i & (1 << (7 - j)) != 0 for j in range(0, 8)]

total_length = int(sys.argv[1])

grid = []
for i in range(0, 128):
    input_string = '{}-{}'.format(sys.argv[2], i)
    output = knot_hash(input_string)
    bits = sum([int_to_bits(x) for x in output], [])
    grid.append(bits)

def explore_region(initial_x, initial_y):
    todo_x = collections.deque([initial_x])
    todo_y = collections.deque([initial_y])
    while len(todo_x):
        x = todo_x.popleft()
        y = todo_y.popleft()
        grid[y][x] = False
        if x > 0 and grid[y][x-1]:
            todo_x.append(x-1)
            todo_y.append(y)
        if x < 127 and grid[y][x+1]:
            todo_x.append(x+1)
            todo_y.append(y)
        if y > 0 and grid[y-1][x]:
            todo_x.append(x)
            todo_y.append(y-1)
        if y < 127 and grid[y+1][x]:
            todo_x.append(x)
            todo_y.append(y+1)

x = 0
y = 0
regions = 0
while y < 128 and x < 128:
    if grid[y][x]:
        regions += 1
        explore_region(x, y)

    x += 1
    if x == 128:
        x = 0
        y += 1

print(regions)

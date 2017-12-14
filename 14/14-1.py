#!/usr/bin/python3

import sys

bit_counts = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

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

    output = ''
    for i in range(0, 16):
        checksum = 0
        for j in range(0, 16):
            checksum ^= string[16 * i + j]
        output += '{:02x}'.format(checksum)

    return output

total_length = int(sys.argv[1])

total = 0
for i in range(0, 128):
    input_string = '{}-{}'.format(sys.argv[2], i)
    output = knot_hash(input_string)
    line_count = sum([bit_counts[int(x, 16)] for x in list(output)])
    print(input_string, line_count)
    total += line_count

print(total)

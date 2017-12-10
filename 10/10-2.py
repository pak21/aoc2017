#!/usr/bin/python3

import sys

def round(string, position, skip):
    for length in lengths:
        new_string = string[:]
        for i in range(0, length):
            new_string[(position + length - 1 - i) % total_length] = string[(position + i) % total_length]
        string = new_string

        position += length + skip
        skip += 1

    return string, position, skip

total_length = int(sys.argv[1])
string = list(range(0, total_length))

lengths = [ord(c) for c in sys.argv[2]]
lengths.extend([17, 31, 73, 47, 23])

position = 0
skip = 0

for i in range(0, 64):
    string, position, skip = round(string, position, skip)

output = ''

for i in range(0, 16):
    checksum = 0
    for j in range(0, 16):
        checksum ^= string[16 * i + j]
    output += '{:02x}'.format(checksum)

print(output)

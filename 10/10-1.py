#!/usr/bin/python3

import sys

total_length = int(sys.argv[1])
string = list(range(0, total_length))

position = 0
skip = 0

with open(sys.argv[2]) as input_file:
    for length in [int(x) for x in input_file.readline().rstrip().split(',')]:

        new_string = string[:]
        for i in range(0, length):
            new_string[(position + length - 1 - i) % total_length] = string[(position + i) % total_length]
        string = new_string

        position += length + skip
        skip += 1

    print(string)
    print(string[0] * string[1])

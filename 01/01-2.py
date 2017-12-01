#!/usr/bin/python3

import sys

with open(sys.argv[1]) as input_file:
    for line in input_file:
        stripped_line = line.rstrip()
        length = len(stripped_line)

        sum = 0

        for i in range(0, length // 2):
            a = stripped_line[i]
            b = stripped_line[i + length // 2]
            if a == b:
                sum += int(a)

        print('{} -> {}'.format(stripped_line, 2 * sum))

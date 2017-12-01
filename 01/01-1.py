#!/usr/bin/python3

import sys

with open(sys.argv[1]) as input_file:
    for line in input_file:
        stripped_line = line.rstrip()
        length = len(stripped_line)

        previous = stripped_line[-1]
        sum = 0

        for i in range(0, length):
            current = stripped_line[i]
            if current == previous:
                sum += int(current)
            previous = current

        print('{} -> {}'.format(stripped_line, sum))

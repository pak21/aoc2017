#!/usr/bin/python3

import sys

with open(sys.argv[1]) as input_file:
    total = 0
    for line in input_file:
        number_strings = line.rstrip().split()
        numbers = [int(s) for s in number_strings]
        min_value = min(numbers)
        max_value = max(numbers)
        difference = max_value - min_value
        total = total + difference
    print(total)

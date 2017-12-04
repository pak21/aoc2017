#!/usr/bin/python3

import sys

with open(sys.argv[1]) as input_file:
    total_valid = 0
    for line in input_file:
        seen = {}
        valid = True
        for word in line.rstrip().split():
            sorted_word = ''.join(sorted(word))
            if sorted_word in seen:
                valid = False
                break
            seen[sorted_word] = True
        print('{} -> {}'.format(line.rstrip(), valid))
        if valid:
            total_valid += 1
    print(total_valid)

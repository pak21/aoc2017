#!/usr/bin/python3

import sys

with open(sys.argv[1]) as input_file:
    for line in input_file:
        score = 0
        level = 0
        garbage = False
        cancelled = False
        garbage_count = 0
        for character in list(line.rstrip()):
            if not cancelled:
                if character == '!':
                    cancelled = True
                else:
                    if garbage:
                        if character == '>':
                            garbage = False
                        else:
                            garbage_count += 1
                    elif character == '<':
                        garbage = True
                    elif character == '{':
                        level += 1
                    elif character == '}':
                        score += level
                        level -= 1
            else:
                cancelled = False

        print('{} {}'.format(score, garbage_count))

#!/usr/bin/python3

import sys

with open(sys.argv[1]) as input_file:
    total = 0
    for line in input_file:
        number_strings = line.rstrip().split()
        numbers = [int(s) for s in number_strings]
        for i in range(0, len(numbers)):
            for j in range(0, i):
                a = numbers[i]
                b = numbers[j]
                if (a // b) * b == a:
                    d = a // b
                elif (b // a) * a == b:
                    d = b // a
        total += d
    print(total)

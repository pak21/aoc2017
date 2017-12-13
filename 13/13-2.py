#!/usr/bin/python3

import sys

depths = []
durations = []

def is_good(delay):
    total_severity = 0
    for i in range(0, len(depths)):
        depth = depths[i]
        duration = durations[i]
        if (depth + delay) % duration == 0:
            return False

    return True

with open(sys.argv[1]) as input_file:
    for line in [l.rstrip() for l in input_file]:
        depth, layer_range = [int(i) for i in line.split(': ')]
        depths.append(depth)
        durations.append(2 * layer_range - 2)

for delay in range(0, 10000000):
    if is_good(delay):
        print(delay)
        break

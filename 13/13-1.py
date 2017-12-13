#!/usr/bin/python3

import sys

depths = []
ranges = []
durations = []

def severity(delay):
    total_severity = 0
    for i in range(0, len(depths)):
        depth = depths[i]
        duration = durations[i]
        if (depth + delay) % duration == 0:
            severity = depth * ranges[i]
            total_severity += severity

    return total_severity

with open(sys.argv[1]) as input_file:
    for line in [l.rstrip() for l in input_file]:
        depth, layer_range = [int(i) for i in line.split(': ')]
        depths.append(depth)
        ranges.append(layer_range)
        durations.append(2 * layer_range - 2)

for delay in range(0, 1000):
    print('{} -> {}'.format(delay, severity(delay)))

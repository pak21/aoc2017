#!/usr/bin/python3

import sys

directions = {
        'ne': 0,
        'n': 1,
        'nw': 2,
        'sw': 3,
        's': 4,
        'se': 5
}

def distance(counts):
    for i in range(0, 3):
        lesser = min(counts[i], counts[i+3])
        counts[i] -= lesser
        counts[i+3] -= lesser

    for d1 in range(0, 6):
        middle = (d1 + 1) % 6
        d2 = (d1 + 2) % 6

        lesser = min(counts[d1], counts[d2])
        counts[d1] -= lesser
        counts[d2] -= lesser
        counts[middle] += lesser

    return sum(counts)

with open(sys.argv[1]) as input_file:
    max_distance = 0
    for line in [l.rstrip() for l in input_file]:
        counts = [0, 0, 0, 0, 0, 0]

        for move in line.split(','):
            counts[directions[move]] += 1
            total_moves = distance(counts)
            if total_moves > max_distance:
                max_distance = total_moves

        print('{} {}'.format(total_moves, max_distance))

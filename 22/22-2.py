#!/usr/bin/python3

import collections
import sys

grid = collections.defaultdict(lambda: collections.defaultdict(int))

x_moves = [0, 1, 0, -1]
y_moves = [-1, 0, 1, 0]

with open(sys.argv[1]) as input_file:
    linenum = 0
    for line in [l.rstrip() for l in input_file]:
        infected = [2 if c == '#' else 0 for c in list(line)]
        offset = (len(infected) - 1) // 2
        for i in range(0, len(infected)):
            grid[linenum - offset][i - offset] = infected[i]
        linenum += 1

x = 0
y = 0
direction = 0

counts = collections.defaultdict(int)

for step in range(0, 10000000):
    dir_change = grid[y][x] - 1
    direction = (direction + dir_change) % 4

    counts[grid[y][x]] += 1
    grid[y][x] = (grid[y][x] + 1) % 4

    x += x_moves[direction]
    y += y_moves[direction]

print(counts)

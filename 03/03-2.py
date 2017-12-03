#!/usr/bin/python3

import collections
import math

def calc(n):
    ring = math.ceil(math.sqrt(n))
    if not ring % 2:
        ring += 1
    ring_max = ring * ring
    offset = ring_max - n
    side_length = ring - 1
    side = offset // side_length
    side_offset = offset % side_length
    fixed = ring // 2
    if side == 0:
        x = fixed - side_offset
        y = -fixed
    elif side == 1:
        x = -fixed
        y = side_offset - fixed
    elif side == 2:
        x = side_offset - fixed
        y = fixed
    else:
        x = fixed
        y = fixed - side_offset

    return (x, y)

values = collections.defaultdict(lambda: collections.defaultdict(int))

values[0][0] = 1
max_value = 1

n = 1
while max_value < 361527:
    n = n + 1
    x, y = calc(n)
    neighbours = ( \
        values[x-1][y+1], values[x  ][y+1], values[x+1][y+1], \
        values[x-1][y  ],                   values[x+1][y  ], \
        values[x-1][y-1], values[x  ][y-1], values[x+1][y-1] )
    value = sum(neighbours)
    values[x][y] = value
    if value > max_value:
        max_value = value
    print('{} {} {} {}'.format(n, x, y, value))

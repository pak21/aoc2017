#!/usr/bin/python3

import sys

def hflip(pattern):
    return [row[::-1] for row in pattern]

def vflip(pattern):
    return pattern[::-1]

def dflip(pattern):
    output = [[None] * len(pattern) for i in range(0, len(pattern))]
    for y in range(0, len(pattern)):
        for x in range(0, len(pattern)):
            output[x][y] = pattern[y][x]
    return output

def generate_pattern(pattern, which):
    if which & 1 == 1:
        pattern = hflip(pattern)
    if which & 2 == 2:
        pattern = vflip(pattern)
    if which & 4 == 4:
        pattern = dflip(pattern)
    return pattern

def make_hash(pattern):
    flat = [i for row in pattern for i in row]
    return sum([(1 << i) if flat[i] else 0 for i in range(0, len(flat))])

rules2 = {}
rules3 = {}

with open(sys.argv[1]) as input_file:
    for line in [l.rstrip() for l in input_file]:
        left, _, right = line.split(' ')
        left_lines = [[c == '#' for c in list(l)] for l in left.split('/')]
        right_lines = [[c == '#' for c in list(l)] for l in right.split('/')]

        hashes = set([make_hash(generate_pattern(left_lines, i)) for i in range(0, 8)])
        target = rules2 if len(left_lines) % 2 == 0 else rules3
        for h in hashes:
            target[h] = right_lines

grid = [[False, True, False], [False, False, True], [True, True, True]]

for iteration in range(0, 18):
    if len(grid) % 2 == 0:
        chunk_count = len(grid) // 2
        new_size = 3 * chunk_count
        new_grid = [[None] * new_size for i in range(0, new_size)]
        for y in range(0, chunk_count):
            for x in range(0, chunk_count):
                chunk = [row[x*2:x*2+2] for row in grid[y*2:y*2+2]]
                new_chunk = rules2[make_hash(chunk)]
                for z in range(0, 3):
                    new_grid[y*3+z][x*3:x*3+3] = new_chunk[z]
        grid = new_grid
    elif len(grid) % 3 == 0:
        chunk_count = len(grid) // 3
        new_size = 4 * chunk_count
        new_grid = [[None] * new_size for i in range(0, new_size)]
        for y in range(0, chunk_count):
            for x in range(0, chunk_count):
                chunk = [row[x*3:x*3+3] for row in grid[y*3:y*3+3]]
                new_chunk = rules3[make_hash(chunk)]
                for z in range(0, 4):
                    new_grid[y*4+z][x*4:x*4+4] = new_chunk[z]
        grid = new_grid

    print(sum([sum(row) for row in grid]))

#!/usr/bin/python3

import operator
import re
import sys

data = []

def sort_for_collisions(unsorted_data):
    return sorted(unsorted_data, key = lambda x: (x[1][0], x[1][1], x[1][2]))

def find_collisions(sorted_data):
    to_remove = set()
    for i in range(0, len(sorted_data) - 1):
        p_a = sorted_data[i][1]
        p_b = sorted_data[i+1][1]
        if p_a == p_b:
            to_remove.add(i)
            to_remove.add(i+1)

    if len(to_remove) > 0:
        to_remove_list = sorted(to_remove, reverse = True)
        for i in to_remove_list:
            del(sorted_data[i])

    return data

def step_particle(x):
    new_v = list(map(sum, zip(x[2], x[3])))
    new_p = list(map(sum, zip(x[1], new_v)))
    return (x[0], new_p, new_v, x[3])

def step(data):
    return [step_particle(x) for x in data]

with open(sys.argv[1]) as input_file:
    linenum = 0
    for line in [l.rstrip() for l in input_file]:
        match = re.match('p=<(.*)>, v=<(.*)>, a=<(.*)>', line)
        p, v, a = [[int(x) for x in g.split(',')] for g in match.groups()]
        tup = (linenum, p, v, a)
        data.append(tup)
        linenum += 1

time = 0
while True:
    time += 1
    data = step(data)
    data = sort_for_collisions(data)
    data = find_collisions(data)
    print(len(data))

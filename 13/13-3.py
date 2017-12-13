#!/usr/bin/python3

import gmpy2
import sys

depths = []
durations = []

class Layer:
    def __init__(self, depth, layer_range):
        self.depth = depth
        self.duration = 2 * layer_range - 2

constraints = {}

with open(sys.argv[1]) as input_file:
    for line in [l.rstrip() for l in input_file]:
        depth, layer_range = [int(i) for i in line.split(': ')]
        duration = 2 * layer_range - 2

        if duration not in constraints:
            constraints[duration] = [True] * duration

        constraints[duration][-depth % duration] = False

to_remove = set()

for k1, v1 in constraints.items():
    remove = False
    for k2 in filter(lambda k: k != k1 and k % k1 == 0, constraints.keys()):
        to_remove.add(k1)

        v2 = constraints[k2]
        for forbidden in filter(lambda x: not v1[x], range(0, k1)):
            for to_forbid in filter(lambda x: x % k1 == forbidden, range(0, k2)):
                constraints[k2][to_forbid] = False

for k in to_remove:
    del constraints[k]

lcm = 1
modulo = 0

to_remove = set()

for k, v in constraints.items():
    all_allowed = list(filter(lambda x: v[x], range(0, k)))
    if len(all_allowed) == 1:
        allowed = all_allowed[0]
        while modulo % k != allowed:
            modulo += lcm
        lcm = gmpy2.lcm(lcm, k)
        to_remove.add(k)

for k in to_remove:
    del constraints[k]

complete = False
while not complete:
    complete = True
    for k, v in constraints.items():
        if not v[modulo % k]:
            complete = False
            break

    if complete:
        break

    modulo += lcm

print(modulo)

#!/usr/bin/python3

import collections
import re
import sys

children = {}
weight = {}
parent = {}
total_weight = {}

def child(s):
    return s[:-1] if s[-1] == ',' else s

def calculate_weight(name):
    for n in children[name]:
        calculate_weight(n)
    total_weight[name] = weight[name] + sum([total_weight[n] for n in children[name]])

with open(sys.argv[1]) as input_file:
    for line in input_file:
        components = line.rstrip().split()
        name = components[0]
        weight[name] = int(components[1][1:-1])
        node_children = [child(s) for s in components[3:]] if len(components) > 3 else []
        children[name] = node_children
        for node_child in node_children:
            parent[node_child] = name
        if name not in parent:
            parent[name] = None

roots = [k for k, v in parent.items() if v == None]
print('Root: {}'.format(roots))

if len(roots) != 1:
    print('Aaargh!')
    sys.exit(1)

calculate_weight(roots[0])

culprit = roots[0]

while True:
    child_weights = [total_weight[name] for name in children[culprit]]
    counts = collections.defaultdict(lambda: 0)
    for w in child_weights:
        counts[w] += 1
    faulty_total_weights = [k for k, v in counts.items() if v == 1]
    if len(faulty_total_weights) != 1:
        break;
    good_total_weight = [k for k, v in counts.items() if v != 1][0]
    faulty_total_weight = faulty_total_weights[0]
    diff = good_total_weight - faulty_total_weight
    culprit = [name for name in children[culprit] if total_weight[name] == faulty_total_weight][0]

target_weight = weight[culprit] + diff
print('{} should have weight {}'.format(culprit, target_weight))

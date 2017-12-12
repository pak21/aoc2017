#!/usr/bin/python3

import collections
import sys

connections = collections.defaultdict(lambda: [])

with open(sys.argv[1]) as input_file:
    for line in [l.rstrip() for l in input_file]:
        words = line.split();
        left = int(words[0])
        right = [int(w.rstrip(',')) for w in words[2:]]

        for r in right:
            connections[left].append(r)

all_items = set(connections.keys())
groups = 0

while len(all_items) > 0:
    groups += 1
    first = all_items.pop()
    todo = collections.deque([first])
    seen = set()

    while len(todo) > 0:
        item = todo.popleft()
        if item in all_items:
            all_items.remove(item)
        seen.add(item)
        for r in connections[item]:
            if not r in seen:
                todo.append(r)

    print('{} -> {}'.format(first, len(seen)))

print(groups)

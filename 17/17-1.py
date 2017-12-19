#!/usr/bin/python3

import sys

step = int(sys.argv[1])

spinlock = [0]
current = 0

for i in range(1, 2018):
    current = (current + step) % len(spinlock)
    current += 1
    spinlock.insert(current, i)

current = (current + 1) % len(spinlock)
print(spinlock[current])

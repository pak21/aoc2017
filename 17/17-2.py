#!/usr/bin/python3

import sys

step = int(sys.argv[1])
length = 1
current = 0

target = None

for i in range(1, 50000001):
    current = (current + step) % length
    if current == 0:
        target = i
    current = current + 1
    length += 1

print(target)

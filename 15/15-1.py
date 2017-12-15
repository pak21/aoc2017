#!/usr/bin/python3

import sys

def iterate(current, factor):
    return (current * factor) % 2147483647

current1 = int(sys.argv[1])
current2 = int(sys.argv[2])

matches = 0
for i in range(0, 40000000):
    current1 = iterate(current1, 16807)
    current2 = iterate(current2, 48271)
    if current1 % 65536 == current2 % 65536:
        matches += 1

print(matches)

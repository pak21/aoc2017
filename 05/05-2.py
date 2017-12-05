#!/usr/bin/python3

import sys

with open(sys.argv[1]) as input_file:
    instructions = []
    for line in input_file:
        instructions.append(int(line))

pc = 0
count = 0
while pc < len(instructions):
    count += 1
    jump = instructions[pc]
    instructions[pc] += 1 if jump < 3 else -1
    pc += jump

print(count)

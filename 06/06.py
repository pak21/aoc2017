#!/usr/bin/python3

import sys

with open(sys.argv[1]) as input_file:
    banks = [int(x) for x in input_file.readline().rstrip().split()]

seen = {}
count = 0

while True:
    count += 1
    max_value = max(banks)
    max_index = banks.index(max_value)
    banks[max_index] = 0
    for i in range(max_index + 1, max_index + max_value + 1):
        banks[i % len(banks)] += 1
    banks_string = str(banks)
    if banks_string in seen:
        break
    seen[banks_string] = count

cycle_size = count - seen[banks_string]
print('{} {}'.format(count, cycle_size))

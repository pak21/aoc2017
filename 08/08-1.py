#!/usr/bin/python3

import collections
import sys

registers = collections.defaultdict(lambda: 0)

comparisions = {
        '==': lambda a, b: a == b,
        '!=': lambda a, b: a != b,
        '>': lambda a, b: a > b,
        '>=': lambda a, b: a >= b,
        '<': lambda a, b: a < b,
        '<=': lambda a, b: a <= b
}

operations = {
        'inc': lambda a, b: a + b,
        'dec': lambda a, b: a - b
}

all_time_max_value = 0

with open(sys.argv[1]) as input_file:
    for line in input_file:
        target, operation, value, _, source, comparision, threshold = line.rstrip().split()
        value = int(value)
        threshold = int(threshold)

        source_value = registers[source]
        comparision_func = comparisions[comparision]
        if comparision_func(source_value, threshold):
            target_value = registers[target]
            operation_func = operations[operation]
            new_target_value = operation_func(target_value, value)
            if new_target_value > all_time_max_value:
                all_time_max_value = new_target_value
            registers[target] = new_target_value

print(max(registers.values()))

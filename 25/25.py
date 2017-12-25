#!/usr/bin/python3

import collections
import re
import sys

def set_state(match, parser):
    parser['tm']['state'] = match.group(1)

def set_step_count(match, parser):
    parser['tm']['step_count'] = int(match.group(1))

def set_current_state(match, parser):
    state = match.group(1)
    parser['current_state'] = state
    parser['tm']['states'][state] = {}

def set_current_value(match, parser):
    value = int(match.group(1))
    parser['current_value'] = value
    parser['tm']['states'][parser['current_state']][value] = {}

def set_write_action(match, parser):
    parser['tm']['states'][parser['current_state']][parser['current_value']]['write'] = int(match.group(1))

def set_move_action(match, parser):
    parser['tm']['states'][parser['current_state']][parser['current_value']]['move'] = 1 if match.group(1) == 'right' else -1

def set_next_state(match, parser):
    parser['tm']['states'][parser['current_state']][parser['current_value']]['next'] = match.group(1)

line_matches = [
        ('^Begin in state ([A-Z])\.$', set_state),
        ('^Perform a diagnostic checksum after (\d+) steps\.$', set_step_count),
        ('^$', lambda m, p: None),
        ('^In state ([A-Z]):$', set_current_state),
        ('^  If the current value is ([01]):$', set_current_value),
        ('^    - Write the value ([01])\.$', set_write_action),
        ('^    - Move one slot to the (left|right)\.$', set_move_action),
        ('^    - Continue with state ([A-Z])\.$', set_next_state)
]

parser = {
        'tm': {
            'states': {},
            'location': 0
            }
        }

with open(sys.argv[1]) as input_file:
    for line in [l.rstrip() for l in input_file]:
        done = False
        for matcher in line_matches:
            match = re.match(matcher[0], line)
            if match:
                matcher[1](match, parser)
                done = True
                break

        if not done:
            print('Unknown line -> {}'.format(line))
            sys.exit(1)

tm = parser['tm']
tape = collections.defaultdict(int)

while tm['step_count'] > 0:
    location = tm['location']
    current_value = tape[location]
    actions = tm['states'][tm['state']][current_value]

    tape[location] = actions['write']
    tm['location'] += actions['move']
    tm['state'] = actions['next']

    tm['step_count'] -= 1

print(sum(tape.values()))

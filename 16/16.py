#!/usr/bin/python3

import sys

def swap(line, arg1, arg2):
    line[arg1], line[arg2] = line[arg2], line[arg1]

def dance(line, commands):
    for command in commands:
        if command[0] == 's':
            arg = int(command[1:])
            line = line[-arg:] + line[0:programs-arg]
        elif command[0] == 'x':
            arg1, arg2 = [int(x) for x in command[1:].split('/')]
            swap(line, arg1, arg2)
        elif command[0] == 'p':
            arg1 = command[1]
            arg2 = command[3]
            loc1 = line.index(arg1)
            loc2 = line.index(arg2)
            swap(line, loc1, loc2)
        else:
            print('Unknown command {}'.format(command))
            sys.exit(1)

    return line

programs = int(sys.argv[1])

line = [chr(97 + i) for i in range(0, programs)]
string = ''.join(line)

with open(sys.argv[2]) as input_file:
    commands = input_file.readline().rstrip().split(',')

seen = {}
iterations = 0

while True:
    seen[string] = iterations
    line = dance(line, commands)
    string = ''.join(line)
    iterations += 1
    if iterations == 1:
        print(string)
    if string in seen:
        old = seen[string]
        break

cycle = iterations - old
modulo = 1000000000 % cycle
answer = old + modulo

for k, v in seen.items():
    if v == answer:
        print(k)
        break

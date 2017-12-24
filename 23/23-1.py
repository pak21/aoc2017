#!/usr/bin/python3

import collections
import sys

class Opcode:
    def __init__(self, opcode, arg1, arg2):
        self.opcode = opcode
        self.arg1 = arg1
        self.arg2 = arg2

    def __repr__(self):
        return '{} {} {}'.format(self.opcode, self.arg1, self.arg2)

def parse_opcode(string):
    words = string.split()
    opcode = words[0]
    arg1 = words[1]
    arg2 = words[2] if len(words) > 2 else None
    return Opcode(opcode, arg1, arg2)

def get_value(arg, registers):
    return registers[arg] if str.isalpha(arg) else int(arg)

def opcode_jnz(arg1, arg2, pc, registers):
    if get_value(arg1, registers) != 0:
        pc += get_value(arg2, registers)
    else:
        pc += 1

    return pc

def opcode_mul(arg1, arg2, pc, registers):
    registers['mul'] += 1
    registers[arg1] *= get_value(arg2, registers)
    return pc + 1

def opcode_set(arg1, arg2, pc, registers):
    registers[arg1] = get_value(arg2, registers)
    return pc + 1

def opcode_sub(arg1, arg2, pc, registers):
    registers[arg1] -= get_value(arg2, registers)
    return pc + 1

opcodes = {
        'jnz': opcode_jnz,
        'mul': opcode_mul,
        'set': opcode_set,
        'sub': opcode_sub
}

def execute_opcode(opcode, pc, registers):
    return opcodes[opcode.opcode](opcode.arg1, opcode.arg2, pc, registers)

with open(sys.argv[1]) as input_file:
    program = [parse_opcode(string.rstrip()) for string in input_file]

pc = 0
registers = collections.defaultdict(lambda: 0)

while pc < len(program):
    pc = execute_opcode(program[pc], pc, registers)

print(registers)

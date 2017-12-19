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

def opcode_add(arg1, arg2, pc, registers, send_queue, receive_queue):
    registers[arg1] += get_value(arg2, registers)
    return pc + 1, False

def opcode_jgz(arg1, arg2, pc, registers, send_queue, receive_queue):
    if get_value(arg1, registers) > 0:
        pc += get_value(arg2, registers)
    else:
        pc += 1

    return pc, False

def opcode_mod(arg1, arg2, pc, registers, send_queue, receive_queue):
    registers[arg1] %= get_value(arg2, registers)
    return pc + 1, False

def opcode_mul(arg1, arg2, pc, registers, send_queue, receive_queue):
    registers[arg1] *= get_value(arg2, registers)
    return pc + 1, False

def opcode_rcv(arg1, arg2, pc, registers, send_queue, receive_queue):
    if len(receive_queue):
        value = receive_queue.popleft()
        registers[arg1] = value
        return pc + 1, False
    else:
        return pc, True

def opcode_set(arg1, arg2, pc, registers, send_queue, receive_queue):
    registers[arg1] = get_value(arg2, registers)
    return pc + 1, False

def opcode_snd(arg1, arg2, pc, registers, send_queue, receive_queue):
    value = get_value(arg1, registers)
    registers['sent'] += 1
    send_queue.append(value)
    return pc + 1, False

opcodes = {
        'add': opcode_add,
        'jgz': opcode_jgz,
        'mod': opcode_mod,
        'mul': opcode_mul,
        'rcv': opcode_rcv,
        'set': opcode_set,
        'snd': opcode_snd
}

def execute_opcode(opcode, pc, registers, send_queue, receive_queue):
    return opcodes[opcode.opcode](opcode.arg1, opcode.arg2, pc, registers, send_queue, receive_queue)

with open(sys.argv[1]) as input_file:
    program = [parse_opcode(string.rstrip()) for string in input_file]

pc = [0, 0]
registers = [
        collections.defaultdict(lambda: 0),
        collections.defaultdict(lambda: 0)
]
queues = [
        collections.deque(),
        collections.deque()
]

registers[1]['p'] = 1

executing = 0
last_switch = False
while True:
    this_pc = pc[executing]
    pc[executing], switch = execute_opcode(program[this_pc], this_pc, registers[executing], queues[executing], queues[1 - executing])
    if switch:
        if last_switch:
            print(registers[1]['sent'])
            break
        executing = 1 - executing
        last_switch = True
    else:
        last_switch = False

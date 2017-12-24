#!/usr/bin/python3

import collections
import sys

class Connector:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __repr__(self):
        return '{}/{}'.format(self.a, self.b)

class Bridge:
    def __init__(self, connectors, port):
        self.connectors = connectors
        self.port = port

    def add_connector(self, new_connector):
        new_connectors = self.connectors.copy()
        new_connectors.add(new_connector)
        new_port = new_connector.a if self.port == new_connector.b else new_connector.b
        return Bridge(new_connectors, new_port)

    def strength(self):
        return sum([c.a + c.b for c in self.connectors])

    def __repr__(self):
        return '{} {}'.format(self.port, self.connectors)

def parse_connector(string):
    a, b = string.split('/')
    return Connector(a, b)

def is_valid_connector(connector, current_bridge):
    return connector not in current_bridge.connectors and (connector.a == current_bridge.port or connector.b == current_bridge.port)

def get_valid_connectors(current_bridge):
    return [connector for connector in connectors if is_valid_connector(connector, current_bridge)]

with open(sys.argv[1]) as input_file:
    connectors = [parse_connector(string.rstrip()) for string in input_file]

initial_bridge = Bridge(set(), 0)
bridges = [initial_bridge]
todo = collections.deque(bridges)

while todo:
    bridge = todo.popleft()
    next_connectors = get_valid_connectors(bridge)
    new_bridges = [bridge.add_connector(c) for c in next_connectors]

    bridges.extend(new_bridges)
    todo.extend(new_bridges)

print(max([b.strength() for b in bridges]))

max_length = max([len(b.connectors) for b in bridges])
print(max([b.strength() for b in bridges if len(b.connectors) == max_length]))

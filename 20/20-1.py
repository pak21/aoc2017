#!/usr/bin/python3

import re
import sys

data = []

with open(sys.argv[1]) as input_file:
    linenum = 0
    for line in [l.rstrip() for l in input_file]:
        match = re.match('p=<(.*)>, v=<(.*)>, a=<(.*)>', line)
        p, v, a = [sum([abs(int(x)) for x in g.split(',')]) for g in match.groups()]
        tup = (linenum, p, v, a)
        data.append(tup)
        linenum += 1

s = sorted(data, key = lambda t: t[3])
print(s[0])
print(s[1])

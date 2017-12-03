#!/usr/bin/python3

import math
import sys

def calc(n):
    f = math.floor(math.sqrt(n - 1))
    d = n - f * f - 1

    if f % 2:
        dp = d % (f + 1)
        m = f - dp if dp < f / 2 else dp + 1
    else:
        dp = d % f
        m = f - dp if dp <= f / 2 else dp
    print('{} {}'.format(n, m))

for n in range(2, 26):
    calc(n)

calc(1024)

for n in range(361520, 361531):
    calc(n)

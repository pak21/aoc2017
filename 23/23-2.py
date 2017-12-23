#!/usr/bin/python3

import gmpy2

print(sum([not gmpy2.is_prime(i) for i in range(108100, 108100 + 17000 + 1, 17)]))

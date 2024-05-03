#!/usr/bin/python3
"""
This script reads from standard input and computes metrics
"""
import sys
from re import match

codes_dict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0}

file_size = 0
counter = 0
reg = r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'


def print_stats():
    """Prints the accumulated stats and resets the counters."""
    print(f'File size: {file_size}')
    for code in sorted(codes_dict.keys()):
        if codes_dict[code] != 0:
            print(f'{code}: {codes_dict[code]}')


try:
    for line in sys.stdin:
        if not match(reg, line):
            continue
        file_size += int(line.split()[-1])
        code = line.split()[-2]
        counter += 1
        if code in codes_dict:
            codes_dict[code] += 1
            if (counter % 10 == 0 and counter != 0):
                print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
print_stats()

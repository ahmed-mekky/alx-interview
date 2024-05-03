#!/usr/bin/python3
import sys
"""
This script reads from standard input and computes metrics
"""
codes_dict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0}
counter = 0
try:
    for line in sys.stdin:
        file_size += int(line.split()[-1])
        code = line.split()[-2]
        counter += 1
        if code in codes_dict:
            codes_dict[code] += 1
            if (counter % 10 == 0 and counter != 0):
                print(f'File size: {file_size}')
                for code in codes_dict.keys():
                    print(f'{code}: {codes_dict[code]}')
except KeyboardInterrupt:
    print(f'File size: {file_size}')
    for code in codes_dict.keys():
        print(f'{code}: {codes_dict[code]}')

#!/usr/bin/python3
"""Calculates the fewest number of operations needed"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n < 2:
        return 0
    main_primes = [2, 3, 5, 7, 9, 11]
    for i in main_primes:
        if n % i == 0:
            if (n / i) in main_primes:
                return i + int(n / i)
            return i + minOperations(int(n / i))
    return n

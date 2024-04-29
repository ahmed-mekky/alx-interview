#!/usr/bin/python3
"""Calculates the fewest number of operations needed"""


def is_prime(n):
    """
    This function checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n < 2:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            if is_prime(i) and is_prime(n // i):
                return i + int(n / i)
            elif is_prime(i):
                return i + minOperations(int(n / i))
    return n

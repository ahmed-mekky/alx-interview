#!/usr/bin/python3
"""making change (coins) module"""


def makeChange(coins, total):
    """main function"""
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    coin = coins[0]
    n = 0
    while True:
        if coin > total:
            if total == 0:
                return n
            elif coin is coins[-1]:
                return -1
            coin = coins[coins.index(coin) + 1]
            continue
        n += 1
        total -= coin

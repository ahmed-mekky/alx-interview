#!/usr/bin/python3
"""Maria and Ben are playing a game.
Given a set of consecutive integers
 starting from 1 up to and including n,
 they take turns choosing a prime number from the set
 and removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game,
 where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
 determine who the winner of each"""


def isWinner(x, nums):
    """isWinner func"""
    if x <= 0 or not nums:
        return None
    players = {'Maria': 0, 'Ben': 0}
    names = list(players.keys())
    for num in nums:
        winner = roundWinner(num)
        if winner:
            players[winner] += 1
    return max(players, key=players.get)


def roundWinner(num):
    """roundWinner func"""
    names = ['Maria', 'Ben']
    if num <= 0:
        return None
    player = names[1]
    primes = getPrimes(num)
    for i in range(num):
        if primes:
            primes.pop()
            player = names[i % 2]
            continue
        return player
    return None


def getPrimes(num):
    """getPrimes func"""
    primes = []
    for i in range(2, num + 1):
        if checkPrime(i):
            primes.append(i)
    return primes


def checkPrime(num):
    """checkPrime func"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True

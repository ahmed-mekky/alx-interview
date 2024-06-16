#!/usr/bin/python3
"""island_perimeter"""


def island_perimeter(grid):
    """main func"""
    length = len(grid)
    sum = 0
    for i in range(length):
        for j in range(length):
            item = grid[i][j]
            if item:
                try:
                    if not grid[i - 1][j]:
                        sum += 1
                    if not grid[i + 1][j]:
                        sum += 1
                    if not grid[i][j + 1]:
                        sum += 1
                    if not grid[i][j - 1]:
                        sum += 1
                except IndexError:
                    return None
    return sum

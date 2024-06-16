#!/usr/bin/python3
"""island_perimeter"""


def island_perimeter(grid):
    """main func"""
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            item = grid[i][j]
            if item:
                try:
                    if i > 0:
                        if not grid[i - 1][j]:
                            sum += 1
                    else:
                        sum += 1
                    if j > 0:
                        if not grid[i][j - 1]:
                            sum += 1
                    else:
                        sum += 1
                    if not grid[i + 1][j]:
                        sum += 1
                    if not grid[i][j + 1]:
                        sum += 1
                except IndexError:
                    sum += 1
    return sum

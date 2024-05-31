#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotates the matrix"""
    length = len(matrix)
    new_matrix = []
    for i in range(length):
        new_matrix.append([])
        for j in range(length):
            new_matrix[i].append(matrix[i][j])
    for i in range(length):
        for j in range(length):
            matrix[j][length - 1 - i] = new_matrix[i][j]

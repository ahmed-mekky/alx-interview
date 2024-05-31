#!/usr/bin/python3
"""Rotate 2D Matrix"""
import copy


def rotate_2d_matrix(matrix):
    length = len(matrix)
    new_matrix = copy.deepcopy(matrix)
    for i in range(length):
        for j in range(length):
            matrix[j][length - 1 - i] = new_matrix[i][j]

#!/usr/bin/python3
"""rotate matrix module"""


def rotate_2d_matrix(matrix):
    """rotate matrix function"""

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in range(len(matrix)):
        matrix[row].reverse()

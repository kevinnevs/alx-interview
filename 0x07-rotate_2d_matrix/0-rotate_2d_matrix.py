#!/usr/bin/python3
"""2D Matrix rotation module.
"""
def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    new_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            new_matrix[j][rows - i - 1] = matrix[i][j]

    for i in range(cols):
        matrix[i] = new_matrix[i]

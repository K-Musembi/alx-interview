#!/usr/bin/env python3
"""nqueens algorithm"""

import sys


def nqueens(n):
    """generate solutions"""
    matrix = [[0] * n for _ in range(n)]
    total_solutions = []
    nqueens_helper(matrix, 0, n, total_solutions)
    return total_solutions


def queen_safety(matrix, row, col, n):
    """check queen is safe"""
    for i in range(col):
        if matrix[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if matrix[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if matrix[i][j] == 1:
            return False

    return True


def nqueens_helper(matrix, col, n, solutions):
    """backtrack function"""
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    result = False
    for i in range(n):
        if queen_safety(matrix, i, col, n):
            matrix[i][col] = 1
            result = nqueens_helper(matrix, col + 1, n, solutions) or result
            matrix[i][col] = 0

    return result


if __name__ == "__main__":
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: nquens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    total_solutions = nqueens(n)
    for solution in total_solutions:
        print(solution)

#!/usr/bin/python3
"""island perimeter algorithm"""


def island_perimeter(grid):
    """find perimeter of grid"""
    perimeter = 0
    previous_row = None
    previous_cell = None

    for row in grid:
        index = 0
        for cell in row:
            if cell == 1:
                perimeter += 4
                if previous_row[index] == 1:
                    perimeter -= 2
                if previous_cell == 1:
                    perimeter -= 2

            previous_cell = cell
            index += 1

        previous_row = row

    return perimeter

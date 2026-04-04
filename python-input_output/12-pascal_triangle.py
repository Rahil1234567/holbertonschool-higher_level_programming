#!/usr/bin/python3
"""Pascal triangle module."""


def pascal_triangle(n):
    """Return list of lists for n size pascal triangle."""
    triangle = []

    for i in range(n):
        row = [1]
        for j in range(1, i + 1):
            val = row[j - 1] * (i - j + 1) // j
            row.append(val)
        triangle.append(row)
    return triangle

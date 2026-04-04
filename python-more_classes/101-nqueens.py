#!/usr/bin/python3
"""Solves the N Queens problem using optimized backtracking."""
import sys


def solve_nqueens(n):
    """Solve n queen problem."""
    def backtrack(row, current):
        """Recursively find valid solutions and append to sol list."""
        if row == n:
            solutions.append(current[:])
            return
        for col in range(n):
            if col in columns or (row + col) in \
                    pos_diagonals or (row - col) in neg_diagonals:
                continue
            columns.add(col)
            pos_diagonals.add(row + col)
            neg_diagonals.add(row - col)
            current.append([row, col])
            backtrack(row + 1, current)
            # Backtrack
            current.pop()
            columns.remove(col)
            pos_diagonals.remove(row + col)
            neg_diagonals.remove(row - col)

    solutions = []
    columns = set()
    pos_diagonals = set()
    neg_diagonals = set()
    backtrack(0, [])
    return solutions


def main():
    """Validate argument inputs when running."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    results = solve_nqueens(n)
    for solution in results:
        print(solution)


main()

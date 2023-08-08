#!/usr/bin/python3

import sys

def solve_nqueens(rows, cols):
    solver = [[]]
    for q in range(rows):
        solver = place_queen(q, cols, solver)
    return solver

def place_queen(q, cols, prev_solver):
    solver_queen = []
    for array in prev_solver:
        for x in range(cols):
            if is_safe(q, x, array):
                solver_queen.append(array + [x])
    return solver_queen

def is_safe(q, x, array):
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column for column in range(q))

def init():
    if len(sys.argv) != 2:
        print("Usage: ./nqueens.py N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        num_queens = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if num_queens < 4:
        print("N must be at least 4")
        sys.exit(1)
    return num_queens

def n_queens():
    num_queens = init()
    solver = solve_nqueens(num_queens, num_queens)
    for array in solver:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)

if __name__ == '__main__':
    n_queens()

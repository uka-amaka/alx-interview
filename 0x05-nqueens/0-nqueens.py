#!/usr/bin/env python3

import sys

def is_safe(board, row, col, N):
    # Check if a queen can be placed in the given cell without attacking others
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True

def print_solution(board, N):
    # Print the solution in the specified format
    for i in range(N):
        line = ["Q" if j == board[i] else "." for j in range(N)]
        print(" ".join(line))
    print()

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []

    def place_queens(row):
        if row == N:
            solutions.append(board.copy())
        else:
            for col in range(N):
                if is_safe(board, row, col, N):
                    board[row] = col
                    place_queens(row + 1)
                    board[row] = -1

    place_queens(0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)

    if not solutions:
        print(f"No solution found for N = {N}")
        sys.exit(1)

    for solution in solutions:
        print_solution(solution, N)

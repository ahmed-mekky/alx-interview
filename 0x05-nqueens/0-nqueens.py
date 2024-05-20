#!/usr/bin/python3
"""N-quens puzzle"""
from sys import argv


def nChecker():
    """checks for input"""
    try:
        if len(argv) < 2:
            print('Usage: nqueens N')
        elif int(argv[1]) < 4:
            print('N must be at least 4')
        else:
            return int(argv[1])
    except ValueError:
        print('N must be a number')
    exit(1)


def queenChecker(board, col, row, N):
    """checks for new queen space"""
    for i in range(col):
        if board[i][row] == 1:
            return False

    for i, j in zip(range(col, -1, -1), range(row, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(col, -1, -1), range(row, N, 1)):
        if board[i][j] == 1:
            return False

    return True


def queenSetter(board, col, N, solutions):
    """sets the new queen"""
    if col >= N:
        solutions.append([row[:] for row in board])
        return
    for row in range(N):
        if queenChecker(board, col, row, N):
            board[col][row] = 1
            if queenSetter(board, col + 1, N, solutions):
                return True
            board[col][row] = 0
    return False


def main():
    """main function"""
    N = nChecker()
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    queenSetter(board, 0, N, solutions)
    queens = []
    for solution in solutions:
        queens.append([])
        for row in solution:
            for queen in row:
                if queen:
                    queens[solutions.index(solution)].append(
                        [solution.index(row), row.index(queen)])

    for queen in queens:
        print(queen)


main()

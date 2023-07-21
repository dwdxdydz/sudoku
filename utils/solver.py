import numpy as np

def pos_checker(x, y, num, board):
    row_n = x - (x % 3)
    col_n = y - (y % 3)

    for i in range (9):
        if board[x][i] == num:
            return False
        
        if board[i][y] == num:
            return False

    for i in range (0, 3):
        for j in range (0, 3):
            if board[row_n + i][col_n + j] == num:
                return False

    return True

def full_solve(board):
    for i in range (9):
        for j in range (9):
            if board[i][j] == 0:
                for n in range (1, 10, 1):
                    if pos_checker(i, j, n, board):
                        board[i][j] = n
                        if not full_solve(board):
                            board[i][j] = 0
                        else:
                            return True
                return False
    return True

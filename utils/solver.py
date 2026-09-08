"""Sudoku validation and a backtracking solver using the MRV heuristic."""

import numpy as np


def validate_board(board) -> np.ndarray:
    board = np.asarray(board, dtype=int)
    if board.shape != (9, 9):
        raise ValueError("Sudoku board must be a 9x9 matrix")
    if np.any((board < 0) | (board > 9)):
        raise ValueError("Sudoku values must be between 0 and 9")
    return board


def pos_checker(x, y, num, board):
    validate_board(board)
    if not 1 <= num <= 9:
        return False
    block = board[x // 3 * 3:x // 3 * 3 + 3, y // 3 * 3:y // 3 * 3 + 3]
    return num not in board[x, :] and num not in board[:, y] and num not in block


def _candidates(row, col, board):
    used = set(board[row, :]) | set(board[:, col])
    used |= set(board[row // 3 * 3:row // 3 * 3 + 3, col // 3 * 3:col // 3 * 3 + 3].flat)
    return [n for n in range(1, 10) if n not in used]


def full_solve(board):
    """Solve in place. Returns True when a valid solution exists."""
    validate_board(board)
    best = None
    best_candidates = None
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                candidates = _candidates(row, col, board)
                if not candidates:
                    return False
                if best_candidates is None or len(candidates) < len(best_candidates):
                    best, best_candidates = (row, col), candidates
        if best_candidates is not None and len(best_candidates) == 1:
            break

    if best is None:
        return True

    row, col = best
    for number in best_candidates:
        board[row, col] = number
        if full_solve(board):
            return True
    board[row, col] = 0
    return False

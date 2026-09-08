"""Sudoku validation and a backtracking solver using the MRV heuristic."""

import numpy as np


def validate_board(board) -> np.ndarray:
    raw_board = np.asarray(board)
    if not np.issubdtype(raw_board.dtype, np.integer):
        raise ValueError("Sudoku values must be integers")
    board = raw_board.astype(int, copy=False)
    if board.shape != (9, 9):
        raise ValueError("Sudoku board must be a 9x9 matrix")
    if np.any((board < 0) | (board > 9)):
        raise ValueError("Sudoku values must be between 0 and 9")
    return board


def _is_consistent(board: np.ndarray) -> bool:
    """Return whether all given values obey Sudoku's row, column, and box rules."""
    for index in range(9):
        row = board[index, :]
        col = board[:, index]
        if len(row[row > 0]) != len(set(row[row > 0])):
            return False
        if len(col[col > 0]) != len(set(col[col > 0])):
            return False
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            block = board[row:row + 3, col:col + 3].flat
            values = [value for value in block if value > 0]
            if len(values) != len(set(values)):
                return False
    return True


def pos_checker(x, y, num, board):
    board = validate_board(board)
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
    board = validate_board(board)
    if not _is_consistent(board):
        return False
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

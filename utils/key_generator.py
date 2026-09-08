"""Generate valid Sudoku puzzles with a unique solution.

The public :func:`gen` function is kept for compatibility with the CLI and UI.
"""

from __future__ import annotations

import random

import numpy as np


_REMOVED_CELLS = {
    "easy": 36,
    "medium": 45,
    "hard": 52,
    "insane": 57,
}


def _base_solution() -> np.ndarray:
    """Return a randomized, complete Sudoku grid."""
    rows = [group * 3 + row for group in random.sample(range(3), 3)
            for row in random.sample(range(3), 3)]
    cols = [group * 3 + col for group in random.sample(range(3), 3)
            for col in random.sample(range(3), 3)]
    numbers = random.sample(range(1, 10), 9)
    return np.array([[numbers[(row * 3 + row // 3 + col) % 9] for col in cols]
                     for row in rows], dtype=int)


def _count_solutions(board: np.ndarray, limit: int = 2) -> int:
    """Count solutions, stopping once ``limit`` solutions have been found."""
    best_cell = None
    best_candidates = None
    for row in range(9):
        for col in range(9):
            if board[row, col] != 0:
                continue
            used = set(board[row, :]) | set(board[:, col])
            used |= set(board[row // 3 * 3:row // 3 * 3 + 3,
                              col // 3 * 3:col // 3 * 3 + 3].flat)
            candidates = [number for number in range(1, 10) if number not in used]
            if not candidates:
                return 0
            if best_candidates is None or len(candidates) < len(best_candidates):
                best_cell, best_candidates = (row, col), candidates

    if best_cell is None:
        return 1

    row, col = best_cell
    count = 0
    for number in best_candidates:
        board[row, col] = number
        count += _count_solutions(board, limit - count)
        if count >= limit:
            break
    board[row, col] = 0
    return count


def gen(level: str = "medium") -> list[list[int]]:
    """Generate a uniquely solvable puzzle for ``level``.

    Difficulty names are case-insensitive: ``easy``, ``medium``, ``hard``, and
    ``insane``.  A ``ValueError`` explains invalid input rather than failing
    later with an unhelpful indexing error.
    """
    if not isinstance(level, str):
        raise ValueError("Difficulty must be one of: easy, medium, hard, insane")
    difficulty = level.lower()
    if difficulty not in _REMOVED_CELLS:
        raise ValueError("Difficulty must be one of: easy, medium, hard, insane")

    puzzle = _base_solution()
    removed = 0
    positions = list(range(81))
    random.shuffle(positions)
    for position in positions:
        if removed == _REMOVED_CELLS[difficulty]:
            break
        row, col = divmod(position, 9)
        value = puzzle[row, col]
        puzzle[row, col] = 0
        if _count_solutions(puzzle) == 1:
            removed += 1
        else:
            puzzle[row, col] = value

    return puzzle.tolist()

import numpy as np
import pytest

from utils.solver import full_solve, pos_checker, validate_board
from utils.key_generator import gen

PUZZLE = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
])


def test_solver_finds_valid_solution():
    board = PUZZLE.copy()
    assert full_solve(board)
    assert np.all(board > 0)
    for i in range(9):
        assert set(board[i]) == set(range(1, 10))
        assert set(board[:, i]) == set(range(1, 10))


def test_invalid_shape_rejected():
    with pytest.raises(ValueError):
        validate_board(np.zeros((8, 9)))


def test_position_checker():
    assert not pos_checker(0, 2, 5, PUZZLE)
    assert pos_checker(0, 2, 4, PUZZLE)


def test_solver_rejects_inconsistent_completed_board():
    board = np.tile(np.arange(1, 10), (9, 1))
    assert not full_solve(board)


def test_generator_accepts_documented_lowercase_difficulties():
    board = np.array(gen("medium"))
    assert board.shape == (9, 9)
    assert np.count_nonzero(board == 0) == 45
    solution = board.copy()
    assert full_solve(solution)


def test_generator_rejects_unknown_difficulty():
    with pytest.raises(ValueError, match="Difficulty"):
        gen("expert")

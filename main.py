#!/usr/bin/env python3
"""CLI entry point for Sudoku generation and solving."""

import argparse

import numpy as np

from utils.board_generator import generate_window
from utils.key_generator import gen
from utils.solver import full_solve


def parse_args():
    parser = argparse.ArgumentParser(description="Generate and solve a Sudoku puzzle.")
    parser.add_argument("-d", "--difficulty", default="Hard", help="Difficulty accepted by the puzzle generator")
    return parser.parse_args()


def main():
    args = parse_args()
    generated_board = np.asarray(gen(args.difficulty)).copy()
    initial_board = generated_board.copy()
    solved_board = generated_board.copy()
    if not full_solve(solved_board):
        raise RuntimeError("Generator produced an unsolvable puzzle")
    generate_window(generated_board, initial_board, solved_board)


if __name__ == "__main__":
    main()

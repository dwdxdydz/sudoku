#!/usr/bin/python3

import argparse
from utils.key_generator import gen
from utils.board_generator import generate_window
from utils.solver import full_solve
import numpy as np


parser = argparse.ArgumentParser(description='args for difficulty', add_help=False)

parser.add_argument('-d', '--difficulty', type=str, default='Hard', action='store', help='set the difficulty')

args = parser.parse_args()

if args.difficulty:
    level = args.difficulty
else:
    level = "Hard"

generated_board = gen(level)
initial_board = np.copy(generated_board)
solved_board = np.copy(generated_board)
full_solve(solved_board)


generate_window(generated_board, initial_board, solved_board)


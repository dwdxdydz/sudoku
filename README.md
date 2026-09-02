# Sudoku Generator & Solver

A Python Sudoku application that generates boards by difficulty, solves them with recursive backtracking, and renders the puzzle through a desktop UI.

## Highlights

- Difficulty-aware puzzle generation
- Recursive backtracking solver
- Separate board, generation, and solving modules
- Command-line difficulty selection
- NumPy-backed board representation

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py --difficulty Hard
```

Supported difficulty names are defined by the generator in `utils/key_generator.py`.

## Architecture

```text
main.py
  ├── key_generator.py   → puzzle generation
  ├── solver.py          → constraint checking + backtracking
  └── board_generator.py → desktop board UI
```

## Tech Stack

**Python · NumPy · Algorithm Design · Backtracking · Tkinter/OpenCV-style UI components**

## Resume Description

**Sudoku Generator & Solver | Python, NumPy, Backtracking**

Developed a modular Sudoku engine that generates difficulty-based puzzles and solves them using recursive backtracking with row, column, and 3×3 sub-grid constraint validation. Separated puzzle generation, solving, and presentation logic to keep the codebase maintainable and reusable.

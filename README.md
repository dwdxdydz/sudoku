# 🧩 Sudoku Generator & Solver

A Python Sudoku application featuring puzzle generation, board validation, an **MRV-optimized backtracking solver**, automated tests, and an optional Streamlit interface.

## Architecture

```text
Puzzle generation
      ↓
Board validation
      ↓
MRV candidate selection
      ↓
Backtracking search
      ↓
Solved board
```

## Features

- Sudoku puzzle generation
- Board validation
- Minimum Remaining Values (MRV) heuristic
- Recursive backtracking solver
- Automated correctness tests
- Command-line interface
- Optional Streamlit UI

## Run

Generate a puzzle from the CLI:

```bash
python main.py --difficulty medium
```

Launch the interactive interface:

```bash
streamlit run app.py
```

Run tests:

```bash
pytest -q
```

## Solver

The solver selects the empty cell with the fewest legal candidates before branching. This **Minimum Remaining Values (MRV)** heuristic reduces unnecessary search compared with scanning empty cells in a fixed order.

## Project structure

- `main.py` — application entry point
- `utils/solver.py` — Sudoku solving logic
- `utils/board_generator.py` — puzzle generation
- `utils/key_generator.py` — supporting puzzle utilities
- `app.py` — Streamlit interface
- `tests/` — automated tests

## Portfolio value

Demonstrates **Python, algorithms, recursion, constraint solving, heuristic search, NumPy, testing, and user-facing application development**.

## Future improvements

- Difficulty scoring based on solver effort
- Multiple-solution detection
- Solver step/backtracking metrics
- Improved UI and puzzle statistics

# 🧩 Sudoku Generator & Solver

## What is this project?

This is a Python Sudoku application that can **create Sudoku puzzles and solve them automatically**.

You can use the project from the command line or open the optional Streamlit interface.

## How does it work?

A Sudoku board has empty cells that need to be filled while following Sudoku's rules: each number must appear only once in its row, column and 3×3 box.

The solver works like this:

```text
Sudoku puzzle
     ↓
Find an empty cell
     ↓
Find numbers that are allowed there
     ↓
Choose the most restricted empty cell
     ↓
Try a possible number
     ↓
Does it lead to a solution?
   ↓          ↓
  Yes         No
   ↓          ↓
Continue   Try another number
     ↓
Solved board
```

## Main features

- Generates Sudoku puzzles
- Validates boards and moves
- Solves puzzles automatically
- Uses an **MRV (Minimum Remaining Values)** strategy to choose cells intelligently
- Uses recursive **backtracking** when a choice leads to a dead end
- Command-line interface
- Optional Streamlit web interface
- Automated tests

## Run it

Generate a puzzle:

```bash
python main.py --difficulty medium
```

Open the interactive interface:

```bash
streamlit run app.py
```

Run tests:

```bash
pytest -q
```

## How the solver makes decisions

A simple solver could always choose the first empty cell it finds.

This project does something smarter.

Suppose one empty cell can accept only `{7}`, while another can accept `{1, 3, 5, 7}`.

The solver chooses the first cell because it has fewer possibilities. This reduces the number of unnecessary guesses.

If a chosen number eventually causes a contradiction, the solver goes back, removes that choice and tries another one.

## Project structure

```text
main.py                    → Application entry point
utils/solver.py            → Solving logic
utils/board_generator.py   → Puzzle generation
utils/key_generator.py     → Supporting puzzle utilities
app.py                     → Streamlit interface
tests/                     → Automated tests
```

## Technical terms explained

**Algorithm** — A step-by-step method for solving a problem. The Sudoku solver follows a defined set of steps to find a valid solution.

**Constraint** — A rule that must be followed. In Sudoku, a number cannot repeat in the same row, column or 3×3 box.

**MRV (Minimum Remaining Values)** — A strategy that chooses the empty cell with the fewest legal choices. This often reduces the amount of searching required.

**Backtracking** — A search method where the program makes a choice, continues, and goes back to an earlier choice if the current path cannot produce a solution.

**Recursion** — When a function calls itself to solve a smaller version of the same problem. The Sudoku solver uses recursion while searching for a solution.

**Candidate** — A number that is currently allowed in an empty Sudoku cell.

**Validation** — Checking whether data follows the required rules. Here, it checks whether a Sudoku board or move is valid.

**Streamlit** — A Python framework used to create the optional interactive web interface.

**NumPy** — A Python library for working with numerical arrays. It is used by parts of the application.

**Unit test** — A small automated check that verifies one part of a program behaves correctly.

## What does this project demonstrate?

The project combines a classic problem-solving algorithm with a user-facing application:

**Puzzle generation → validation → intelligent search → backtracking → solution**

It demonstrates **Python, algorithms, recursion, constraint solving, heuristic search, testing and application development**.

## Future improvements

- Difficulty scoring based on how much solving effort is required
- Detect puzzles with multiple solutions
- Show solver steps and backtracking statistics
- Improve the interface and puzzle statistics

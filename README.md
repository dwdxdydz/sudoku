# 🧩 Sudoku Generator & Solver

## What is this project?

This is a Python Sudoku application that can **create Sudoku puzzles and solve them automatically**.

You can use it from the command line or open the optional Streamlit interface.

The project is useful for learning how a program can solve a problem by following rules, making choices and correcting those choices when they lead to a dead end.

## Sudoku in simple terms

A Sudoku board contains empty cells. The goal is to fill them with numbers from 1 to 9 while following three rules:

- A number cannot repeat in the same row.
- A number cannot repeat in the same column.
- A number cannot repeat in the same 3×3 box.

The program checks these rules while solving the puzzle.

## How does the solver work?

```text
Sudoku puzzle
     ↓
Find an empty cell
     ↓
Find numbers allowed in that cell
     ↓
Choose the cell with the fewest choices
     ↓
Try a possible number
     ↓
Continue solving
     ↓
Did we reach a dead end?
   ↙             ↘
 No              Yes
 ↓                 ↓
Continue       Go back and try another number
        ↓
     Solved board
```

The solver does not simply guess randomly. It uses **MRV (Minimum Remaining Values)** to choose a useful cell before making a decision.

If a decision later causes a contradiction, it uses **backtracking** to return to an earlier decision and try another option.

## Simple example of the strategy

Imagine two empty cells:

```text
Cell A → {7}
Cell B → {1, 3, 5, 7}
```

Cell A has only one possible number, so the solver chooses Cell A first.

This is useful because solving the most restricted cell first can reduce unnecessary searching.

## Main features

- Generates Sudoku puzzles.
- Validates boards and moves.
- Solves puzzles automatically.
- Uses MRV to choose cells intelligently.
- Uses recursive backtracking when a choice leads to a dead end.
- Provides a command-line interface.
- Provides an optional Streamlit web interface.
- Includes automated tests.

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

## Project structure

```text
main.py                    → Application entry point
utils/solver.py            → Sudoku solving logic
utils/board_generator.py   → Puzzle generation
utils/key_generator.py     → Supporting puzzle utilities
app.py                     → Streamlit interface
tests/                     → Automated tests
```

## Main technologies

- **Python** — application and solving logic
- **NumPy** — numerical array operations used by parts of the project
- **Streamlit** — optional interactive web interface
- **Pytest** — automated testing

## Technical terms explained

**Algorithm** — A step-by-step method for solving a problem. The Sudoku solver follows a specific set of steps to find a valid solution.

**Constraint** — A rule that must always be followed. In Sudoku, the constraints are the row, column and 3×3 box rules.

**Candidate** — A number that is currently allowed in an empty cell.

**MRV (Minimum Remaining Values)** — A strategy that chooses the empty cell with the fewest possible candidates. The idea is to make the most restricted decision first.

**Backtracking** — A search technique where the program makes a choice, continues from that choice, and goes back when it discovers that the choice cannot lead to a valid solution.

**Recursion** — When a function calls itself to solve another part of the same problem. The Sudoku solver uses recursion while exploring possible solutions.

**Search** — Trying possible choices until a valid solution is found.

**Contradiction** — A situation where the current choices violate Sudoku rules or leave an empty cell with no valid candidate.

**Validation** — Checking whether data follows a set of rules. Here it is used to check Sudoku boards and moves.

**Heuristic** — A strategy that helps a program decide what to try first. MRV is a heuristic because it helps reduce unnecessary searching.

**Streamlit** — A Python framework for creating interactive web applications without having to build the frontend from scratch.

**NumPy** — A Python library for working with numerical arrays and mathematical operations.

**Unit test** — A small automated check that verifies whether a particular part of a program behaves correctly.

## What does this project demonstrate?

The project connects a classic algorithm with a usable application:

**Puzzle generation → validation → intelligent choice → backtracking → solution**

It demonstrates practical **Python, algorithms, recursion, constraint solving, heuristic search, testing and application development** skills.

## Future improvements

- Calculate difficulty based on actual solving effort.
- Detect puzzles with multiple solutions.
- Show solver steps and backtracking statistics.
- Improve the interface and puzzle statistics.

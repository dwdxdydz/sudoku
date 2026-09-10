# 🧩 Sudoku Generator & Solver

## What is this project?

This is a Python application that can **create Sudoku puzzles and solve them automatically**.

You can generate a puzzle, check whether a Sudoku board is valid, and let the program find the solution.

It also includes an optional web interface so the project can be used more like a small application instead of only from the terminal.

## How does it work?

```text
Create Sudoku puzzle
        ↓
Check the board
        ↓
Find an empty cell
        ↓
Find numbers that can legally go there
        ↓
Choose the cell with the fewest choices
        ↓
Try a number
        ↓
Does it lead to a solution?
   ↙              ↘
 Yes               No
  ↓                 ↓
Continue       Try another number
        ↓
Solved Sudoku
```

## How does the solver know what number to use?

The program follows the normal Sudoku rules:

- Every row must contain the numbers 1–9 without repetition.
- Every column must contain the numbers 1–9 without repetition.
- Every 3×3 box must contain the numbers 1–9 without repetition.

When there is more than one possible empty cell, the solver chooses the cell with the **fewest possible numbers** first.

This is called the **Minimum Remaining Values (MRV)** strategy. In simple terms, it means:

> Solve the hardest-looking empty cell first.

If a choice eventually makes the puzzle impossible, the program goes back and tries another choice. This is called **backtracking**.

## What can it do?

- Generate Sudoku puzzles.
- Support different difficulty levels.
- Check whether a board is valid.
- Automatically solve puzzles.
- Use MRV to reduce unnecessary trial and error.
- Run from the command line.
- Provide an optional Streamlit web interface.
- Run automated tests.

## Run it

Generate a puzzle:

```bash
python main.py --difficulty medium
```

Start the web interface:

```bash
streamlit run app.py
```

Run tests:

```bash
pytest -q
```

## Project structure

```text
main.py                    → Main application
utils/solver.py            → Sudoku solving logic
utils/board_generator.py   → Puzzle generation
utils/key_generator.py     → Supporting puzzle utilities
app.py                     → Web interface
tests/                     → Automated tests
```

## Main technologies

- **Python** — application logic
- **NumPy** — works with the Sudoku board
- **Streamlit** — optional web interface
- **Backtracking** — searches for a valid solution
- **MRV** — chooses the best cell to solve next

## Why this project is useful

Sudoku looks simple, but solving it efficiently is a good example of a **constraint-solving problem**: every choice has to follow several rules at the same time.

This project demonstrates how a program can make decisions, detect when a decision is wrong, go back, and try another option.

## What I learned

The project demonstrates:

- Algorithms
- Recursion
- Backtracking
- Constraint solving
- Heuristic search
- Input validation
- Testing
- Building a small user-facing application

## Future improvements

- Measure puzzle difficulty based on how much searching is required.
- Detect puzzles with multiple solutions.
- Show the solver's steps to the user.
- Add solving statistics.
- Improve the web interface.

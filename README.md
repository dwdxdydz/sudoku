# Sudoku Generator & Solver

A Python Sudoku project with puzzle generation, validation, an MRV-optimized backtracking solver, automated tests, and an optional Streamlit interface.

## Run

CLI generation:

```bash
python main.py --difficulty medium
```

Interactive UI:

```bash
streamlit run app.py
```

Tests:

```bash
pytest -q
```

## Solver

The solver chooses the empty cell with the fewest legal candidates (Minimum Remaining Values / MRV) before backtracking. This reduces unnecessary branching compared with scanning every empty cell in fixed order.

## Portfolio highlights

- Constraint-solving and recursion
- NumPy-based board validation
- Heuristic search
- Test-driven correctness checks
- Simple user-facing UI

"""Optional Streamlit UI for generating and solving Sudoku boards."""

import streamlit as st
import numpy as np

from utils.key_generator import gen
from utils.solver import full_solve

st.set_page_config(page_title="Sudoku Solver", page_icon="🧩")
st.title("🧩 Sudoku Generator & Solver")
level = st.selectbox("Difficulty", ["easy", "medium", "hard"])

if st.button("Generate puzzle"):
    board = np.array(gen(level))
    st.session_state["puzzle"] = board

if "puzzle" in st.session_state:
    puzzle = st.session_state["puzzle"]
    st.subheader("Puzzle")
    st.code("\n".join(" ".join("." if x == 0 else str(x) for x in row) for row in puzzle))
    if st.button("Solve puzzle"):
        solved = puzzle.copy()
        if full_solve(solved):
            st.subheader("Solution")
            st.code("\n".join(" ".join(str(x) for x in row) for row in solved))
        else:
            st.error("This board has no solution.")

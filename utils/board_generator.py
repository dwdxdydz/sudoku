import pygame
import random
import numpy as np

width = 825
background_c = (230, 230, 230)
background_hint = (240, 240, 240)
white = (230, 230, 230)
black = (0, 0, 0)
hint_c = (50, 50, 50)

# Global variable for input mode and for tracking the status of the puzzle
input_mode = False
puzzle_solved = False

empty_cells = []

def draw_board(win):
    for i in range(0, 10):
        thickness = 5 if i % 3 == 0 else 2
        pygame.draw.line(win, black, (75 + 75 * i, 75), (75 + 75 * i, 750), thickness)
        pygame.draw.line(win, black, (75, 75 * i + 75), (750, 75 * i + 75), thickness)

def get_hint(sudoku_board, final_board):

    if empty_cells:
        row, col = random.choice(empty_cells)
        sudoku_board[row][col] = final_board[row][col]
        return

def generate_window(sudoku_board, initial_board, final_board):
    global input_mode, puzzle_solved, empty_cells
    pygame.init()
    win = pygame.display.set_mode((width, width+100))
    pygame.display.set_caption("Game")
    win.fill(background_c)

    draw_board(win)

    pygame.display.update()

    while True:
        # Clear the board
        win.fill(background_c)
        draw_board(win)

        # Draw the numbers on the board
        for i in range(9):
            for j in range(9):
                if sudoku_board[i][j] != 0:
                    font = pygame.font.SysFont('Monospace', 30)
                    color = hint_c if (i, j) in empty_cells else black
                    text = font.render(str(sudoku_board[i][j]), True, color)
                    win.blit(text, (97.5 + j * 75, 90 + i * 75))

        # Draw the hint button
        pygame.draw.rect(win, black, (75, 800, 75, 45))
        font = pygame.font.SysFont('Arial', 25)
        text = font.render("Hint", True, white)
        win.blit(text, (85, 815))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Handle user input
            if not puzzle_solved:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        # Get the row and column of the clicked cell
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        row = (mouse_y - 75) // 75
                        col = (mouse_x - 75) // 75

                        # Check if the cell is empty (0) in the Sudoku board
                        if 0 <= row < 9 and 0 <= col < 9 and initial_board[row][col] == 0:
                            input_mode = True  # Enable input mode
                        elif 75 <= mouse_x <= 150 and 800 <= mouse_y <= 845:
                            # The mouse click is inside the "Hint" button area
                            if not puzzle_solved:
                                get_hint(sudoku_board, final_board)

            if input_mode and event.type == pygame.KEYDOWN and not puzzle_solved:
                # print(np.matrix(board))
                if pygame.K_1 <= event.key <= pygame.K_9:
                    # Set the cell to the input number
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    row = (mouse_y - 75) // 75
                    col = (mouse_x - 75) // 75
                    sudoku_board[row][col] = int(pygame.key.name(event.key))
                    input_mode = False  # Disable input mode

        # Check if the board is filled and correct
        if np.array_equal(sudoku_board, final_board):
            # Board is filled and correct
            font = pygame.font.SysFont('Arial', 40)
            text = font.render("Sudoku Solved!", True, (0, 128, 0))
            win.blit(text, (width // 2 - text.get_width() // 2, width + 20))
            puzzle_solved = True

        for i in range(9):
            for j in range(9):
                if sudoku_board[i][j] == 0:
                    empty_cells.append((i, j))

        pygame.display.update()

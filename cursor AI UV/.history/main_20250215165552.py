import streamlit as st
import pygame
import numpy as np
import time
import random

# Game Constants
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * GRID_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

# Colors
COLORS = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'CYAN': (0, 255, 255),
    'GRID': (50, 50, 50)
}

class TetrisGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.reset_game()

    def reset_game(self):
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.create_piece()
        self.score = 0
        self.game_over = False

    def create_piece(self):
        # Simple piece for testing
        return {
            'shape': [(0,0), (1,0), (0,1), (1,1)],  # Square shape
            'color': COLORS['CYAN'],
            'x': GRID_WIDTH // 2 - 1,
            'y': 0
        }

    def move_piece(self, dx, dy):
        if self.game_over:
            return False

        self.current_piece['x'] += dx
        self.current_piece['y'] += dy

        if not self.is_valid_position():
            self.current_piece['x'] -= dx
            self.current_piece['y'] -= dy
            if dy > 0:  # If moving down, place the piece
                self.place_piece()
            return False
        return True

    def is_valid_position(self):
        for block_x, block_y in self.current_piece['shape']:
            x = self.current_piece['x'] + block_x
            y = self.current_piece['y'] + block_y

            if not (0 <= x < GRID_WIDTH and y < GRID_HEIGHT):
                return False
            if y >= 0 and self.grid[y][x] is not None:
                return False
        return True

    def place_piece(self):
        for block_x, block_y in self.current_piece['shape']:
            x = self.current_piece['x'] + block_x
            y = self.current_piece['y'] + block_y
            if y >= 0:
                self.grid[y][x] = self.current_piece['color']

        self.clear_lines()
        self.current_piece = self.create_piece()
        if not self.is_valid_position():
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        y = GRID_HEIGHT - 1
        while y >= 0:
            if all(cell is not None for cell in self.grid[y]):
                self.grid.pop(y)
                self.grid.insert(0, [None] * GRID_WIDTH)
                lines_cleared += 1
                self.score += 100
            else:
                y -= 1

    def update(self):
        if not self.game_over:
            self.move_piece(0, 1)

    def draw(self):
        # Clear screen
        self.surface.fill(COLORS['BLACK'])

        # Draw grid
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                pygame.draw.rect(
                    self.surface,
                    COLORS['GRID'],
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    1
                )

        # Draw placed blocks
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    pygame.draw.rect(
                        self.surface,
                        self.grid[y][x],
                        (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
                    )

        # Draw current piece
        if self.current_piece:
            for block_x, block_y in self.current_piece['shape']:
                x = self.current_piece['x'] + block_x
                y = self.current_piece['y'] + block_y
                if y >= 0:
                    pygame.draw.rect(
                        self.surface,
                        self.current_piece['color'],
                        (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
                    )

        # Convert surface to numpy array
        view = pygame.surfarray.array3d(self.surface)
        return np.transpose(view, [1, 0, 2])

def main():
    st.set_page_config(page_title="Tetris", layout="wide")
    st.title("Tetris Game")

    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = TetrisGame()
        st.session_state.last_update = time.time()

    # Create two columns
    col1, col2 = st.columns([3, 1])

    with col1:
        # Game board
        game_canvas = st.empty()

    with col2:
        # Controls and score
        st.subheader("Score")
        score_text = st.empty()
        score_text.write(f"Score: {st.session_state.game.score}")

        st.subheader("Controls")
        cols = st.columns(3)
        
        with cols[0]:
            if st.button("⬅️"):
                st.session_state.game.move_piece(-1, 0)
        with cols[1]:
            if st.button("⬇️"):
                st.session_state.game.move_piece(0, 1)
        with cols[2]:
            if st.button("➡️"):
                st.session_state.game.move_piece(1, 0)

        if st.button("New Game"):
            st.session_state.game.reset_game()

        if st.session_state.game.game_over:
            st.error("Game Over!")

    # Game loop
    current_time = time.time()
    if current_time - st.session_state.last_update > 0.5:  # Update every 500ms
        st.session_state.game.update()
        st.session_state.last_update = current_time

    # Draw game
    try:
        game_canvas.image(st.session_state.game.draw())
        score_text.write(f"Score: {st.session_state.game.score}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
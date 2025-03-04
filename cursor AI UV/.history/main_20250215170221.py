import streamlit as st
import numpy as np
import time
from src.tetromino import Tetromino
from src.board import Board
from src.constants import INITIAL_SPEED, POINTS_PER_LINE

class TetrisGame:
    def __init__(self):
        self.board = Board()
        self.score = 0
        self.level = 1
        self.game_over = False
        self.speed = INITIAL_SPEED
        self.spawn_piece()

    def spawn_piece(self):
        self.board.current_piece = Tetromino()
        if not self.board.is_valid_move(self.board.current_piece):
            self.game_over = True

    def move(self, dx, dy):
        if self.game_over:
            return
            
        piece = self.board.current_piece
        piece.move(dx, dy)
        
        if not self.board.is_valid_move(piece):
            piece.move(-dx, -dy)
            if dy > 0:
                self.board.place_piece(piece)
                lines_cleared = self.board.clear_lines()
                self.score += lines_cleared * POINTS_PER_LINE
                self.spawn_piece()

    def rotate(self):
        if self.game_over:
            return
            
        piece = self.board.current_piece
        piece.rotate()
        if not self.board.is_valid_move(piece):
            for _ in range(3):  # Rotate back
                piece.rotate()

    def update(self):
        if not self.game_over:
            self.move(0, 1)

def main():
    st.set_page_config(page_title="Tetris", layout="wide")
    st.title("Tetris Game")

    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = TetrisGame()
        st.session_state.last_update = time.time()

    # Create layout
    col1, col2 = st.columns([3, 1])

    with col1:
        game_canvas = st.empty()

    with col2:
        # Score and controls
        st.subheader(f"Score: {st.session_state.game.score}")
        
        if st.session_state.game.game_over:
            st.error("Game Over!")
        
        # Controls
        st.subheader("Controls")
        cols = st.columns(3)
        
        with cols[0]:
            if st.button("⬅️"):
                st.session_state.game.move(-1, 0)
        with cols[1]:
            if st.button("⬇️"):
                st.session_state.game.move(0, 1)
        with cols[2]:
            if st.button("➡️"):
                st.session_state.game.move(1, 0)
                
        if st.button("Rotate"):
            st.session_state.game.rotate()
            
        if st.button("New Game"):
            st.session_state.game = TetrisGame()
            st.session_state.last_update = time.time()

    # Game loop
    current_time = time.time()
    if current_time - st.session_state.last_update > (st.session_state.game.speed / 1000):
        st.session_state.game.update()
        st.session_state.last_update = current_time

    # Draw game
    game_canvas.image(st.session_state.game.board.draw())

if __name__ == "__main__":
    main() 
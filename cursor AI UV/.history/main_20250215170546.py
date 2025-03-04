import streamlit as st
import numpy as np
import time
from src.tetromino import Tetromino
from src.board import Board
from src.constants import INITIAL_SPEED, POINTS_PER_LINE, POINTS, LINES_PER_LEVEL, SPEED_INCREASE, MIN_SPEED

class TetrisGame:
    def __init__(self):
        self.board = Board()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.paused = False
        self.speed = INITIAL_SPEED
        self._spawn_pieces()

    def _spawn_pieces(self):
        """Spawn current and next pieces"""
        if not self.board.current_piece:
            self.board.current_piece = self.board.next_piece or Tetromino()
        self.board.next_piece = Tetromino()

    def hard_drop(self):
        """Instantly drop the piece to the bottom"""
        if self.game_over or self.paused:
            return
            
        while self.move(0, 1):
            self.score += POINTS['HARD_DROP']

    def update_level(self):
        """Update level based on lines cleared"""
        self.level = (self.lines_cleared // LINES_PER_LEVEL) + 1
        self.speed = max(MIN_SPEED, INITIAL_SPEED - (self.level - 1) * SPEED_INCREASE)

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
                self.lines_cleared += lines_cleared
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
    
    # Add custom CSS for better appearance
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            height: 50px;
            margin: 5px 0;
        }
        .game-container {
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Tetris")

    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = TetrisGame()
        st.session_state.last_update = time.time()

    # Create layout
    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        game_canvas = st.empty()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Game info
        st.subheader("Score")
        score_text = st.empty()
        
        st.subheader("Level")
        level_text = st.empty()
        
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
        
        if st.button("Rotate (↑)"):
            st.session_state.game.rotate()
            
        if st.button("Hard Drop (Space)"):
            st.session_state.game.hard_drop()
            
        if st.button("New Game"):
            st.session_state.game = TetrisGame()

    # Game loop
    current_time = time.time()
    if current_time - st.session_state.last_update > (st.session_state.game.speed / 1000):
        st.session_state.game.update()
        st.session_state.last_update = current_time

    # Draw game
    game_canvas.image(st.session_state.game.board.draw())

if __name__ == "__main__":
    main() 
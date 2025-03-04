import numpy as np
import pygame
from .board import Board
from .tetromino import Tetromino
from .constants import (
    BLOCK_SIZE, BOARD_WIDTH, BOARD_HEIGHT,
    WINDOW_WIDTH, WINDOW_HEIGHT
)

class TetrisGame:
    def __init__(self):
        self.board = Board()
        self.current_piece = Tetromino()
        self.score = 0
        self.game_over = False
        
        # Initialize Pygame surface for drawing
        pygame.init()
        self.surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        
    def handle_input(self, key):
        """Handle keyboard input"""
        if self.game_over:
            return
            
        if key == "ArrowLeft":
            self.move(-1, 0)
        elif key == "ArrowRight":
            self.move(1, 0)
        elif key == "ArrowDown":
            self.move(0, 1)
        elif key == "ArrowUp":
            self.rotate()
        elif key == " ":  # Space
            self.hard_drop()
    
    def update(self):
        """Update game state"""
        if self.game_over:
            return
            
        # Move current piece down
        self.move(0, 1)
    
    def move(self, dx, dy):
        """Move the current piece"""
        self.current_piece.move(dx, dy)
        if not self.board.is_valid_move(self.current_piece):
            self.current_piece.move(-dx, -dy)
            if dy > 0:
                self.place_piece()
    
    def rotate(self):
        """Rotate the current piece"""
        self.current_piece.rotate()
        if not self.board.is_valid_move(self.current_piece):
            for _ in range(3):
                self.current_piece.rotate()
    
    def hard_drop(self):
        """Drop the piece to the bottom"""
        while self.board.is_valid_move(self.current_piece):
            self.current_piece.move(0, 1)
        self.current_piece.move(0, -1)
        self.place_piece()
    
    def place_piece(self):
        """Place the current piece on the board"""
        self.board.place_tetromino(self.current_piece)
        lines_cleared = self.board.clear_lines()
        self.score += lines_cleared * 100
        
        self.current_piece = Tetromino()
        if not self.board.is_valid_move(self.current_piece):
            self.game_over = True
    
    def draw_board(self):
        """Draw the game board and return as an image"""
        self.surface.fill((0, 0, 0))
        
        # Draw board grid
        for y in range(self.board.height):
            for x in range(self.board.width):
                color = self.board.grid[y][x]
                if color:
                    pygame.draw.rect(
                        self.surface,
                        pygame.Color(color),
                        (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
                    )
        
        # Draw current piece
        for x, y in self.current_piece.get_positions():
            if y >= 0:
                pygame.draw.rect(
                    self.surface,
                    pygame.Color(self.current_piece.color),
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
                )
        
        # Convert Pygame surface to numpy array for Streamlit
        view = pygame.surfarray.array3d(self.surface)
        return np.transpose(view, [1, 0, 2]) 
import streamlit as st
import pygame
import numpy as np
import time
import random

# Game Constants
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
WINDOW_WIDTH = BLOCK_SIZE * BOARD_WIDTH
WINDOW_HEIGHT = BLOCK_SIZE * BOARD_HEIGHT

# Colors
COLORS = {
    'I': (0, 240, 240),  # Cyan
    'O': (240, 240, 0),  # Yellow
    'T': (160, 0, 240),  # Purple
    'S': (0, 240, 0),    # Green
    'Z': (240, 0, 0),    # Red
    'J': (0, 0, 240),    # Blue
    'L': (240, 160, 0)   # Orange
}

# Shapes
SHAPES = {
    'I': [(0, 0), (0, 1), (0, 2), (0, 3)],
    'O': [(0, 0), (0, 1), (1, 0), (1, 1)],
    'T': [(0, 1), (1, 0), (1, 1), (1, 2)],
}

class TetrisGame:
    def __init__(self):
        self.reset_game()
        pygame.init()
        self.surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        
    def reset_game(self):
        self.board = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.game_over = False
        self.current_piece = self.new_piece()
        
    def new_piece(self):
        shape_name = random.choice(list(SHAPES.keys()))
        return {
            'shape': SHAPES[shape_name],
            'color': COLORS[shape_name],
            'x': BOARD_WIDTH // 2 - 1,
            'y': 0
        }
        
    def move_piece(self, dx):
        if self.game_over:
            return
        self.current_piece['x'] += dx
        if self.check_collision():
            self.current_piece['x'] -= dx
            
    def rotate_piece(self):
        if self.game_over:
            return
        old_shape = self.current_piece['shape']
        # Rotate the piece
        new_shape = []
        for x, y in old_shape:
            new_shape.append((-y, x))
        self.current_piece['shape'] = new_shape
        if self.check_collision():
            self.current_piece['shape'] = old_shape
            
    def check_collision(self):
        for x, y in self.current_piece['shape']:
            new_x = self.current_piece['x'] + x
            new_y = self.current_piece['y'] + y
            if (new_y >= BOARD_HEIGHT or 
                new_x < 0 or 
                new_x >= BOARD_WIDTH or 
                (new_y >= 0 and self.board[new_y][new_x] is not None)):
                return True
        return False
        
    def update(self):
        if self.game_over:
            return
            
        self.current_piece['y'] += 1
        if self.check_collision():
            self.current_piece['y'] -= 1
            self.place_piece()
            self.current_piece = self.new_piece()
            if self.check_collision():
                self.game_over = True
                
    def place_piece(self):
        for x, y in self.current_piece['shape']:
            board_y = self.current_piece['y'] + y
            board_x = self.current_piece['x'] + x
            if board_y >= 0:
                self.board[board_y][board_x] = self.current_piece['color']
        self.clear_lines()
        
    def clear_lines(self):
        lines_cleared = 0
        y = BOARD_HEIGHT - 1
        while y >= 0:
            if all(cell is not None for cell in self.board[y]):
                self.board.pop(y)
                self.board.insert(0, [None] * BOARD_WIDTH)
                lines_cleared += 1
                self.score += 100
            else:
                y -= 1
                
    def draw(self):
        self.surface.fill((0, 0, 0))
        
        # Draw board
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.board[y][x]:
                    pygame.draw.rect(
                        self.surface,
                        self.board[y][x],
                        (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
                    )
        
        # Draw current piece
        if self.current_piece:
            for x, y in self.current_piece['shape']:
                pygame.draw.rect(
                    self.surface,
                    self.current_piece['color'],
                    ((self.current_piece['x'] + x) * BLOCK_SIZE,
                     (self.current_piece['y'] + y) * BLOCK_SIZE,
                     BLOCK_SIZE - 1, BLOCK_SIZE - 1)
                )
        
        # Convert to numpy array for Streamlit
        view = pygame.surfarray.array3d(self.surface)
        return np.transpose(view, [1, 0, 2])

def main():
    st.set_page_config(page_title="Tetris", layout="wide")
    st.title("Tetris Game")
    
    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = TetrisGame()
        st.session_state.last_update = time.time()
    
    # Create columns for layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Game board
        game_canvas = st.empty()
    
    with col2:
        # Controls
        st.write(f"Score: {st.session_state.game.score}")
        
        if st.button("New Game"):
            st.session_state.game.reset_game()
            
        if st.button("Move Left"):
            st.session_state.game.move_piece(-1)
            
        if st.button("Move Right"):
            st.session_state.game.move_piece(1)
            
        if st.button("Rotate"):
            st.session_state.game.rotate_piece()
    
    # Game loop
    current_time = time.time()
    if current_time - st.session_state.last_update > 0.5:  # Update every 500ms
        st.session_state.game.update()
        st.session_state.last_update = current_time
    
    # Draw game
    game_canvas.image(st.session_state.game.draw())

if __name__ == "__main__":
    main() 
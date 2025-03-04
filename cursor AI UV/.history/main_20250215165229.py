import streamlit as st
import pygame
import numpy as np
import time

# Game Constants
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
WINDOW_WIDTH = BLOCK_SIZE * GRID_WIDTH
WINDOW_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

class SimpleGame:
    def __init__(self):
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.score = 0
        pygame.init()
        self.surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        # Add a test block
        self.block_x = GRID_WIDTH // 2
        self.block_y = 0
        
    def update(self):
        # Move block down
        if self.block_y < GRID_HEIGHT - 1:
            self.block_y += 1
            
    def draw(self):
        # Fill background
        self.surface.fill((0, 0, 0))
        
        # Draw grid lines
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                pygame.draw.rect(
                    self.surface,
                    (50, 50, 50),
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    1
                )
        
        # Draw test block
        pygame.draw.rect(
            self.surface,
            (255, 0, 0),
            (self.block_x * BLOCK_SIZE, self.block_y * BLOCK_SIZE, 
             BLOCK_SIZE - 1, BLOCK_SIZE - 1)
        )
        
        # Convert to numpy array for Streamlit
        view = pygame.surfarray.array3d(self.surface)
        return np.transpose(view, [1, 0, 2])

def main():
    st.set_page_config(page_title="Simple Tetris", layout="wide")
    st.title("Simple Tetris Test")
    
    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = SimpleGame()
        st.session_state.last_update = time.time()
    
    # Create layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Game board
        game_canvas = st.empty()
    
    with col2:
        # Controls
        st.write("Test Controls")
        if st.button("Reset"):
            st.session_state.game = SimpleGame()
    
    # Game loop
    current_time = time.time()
    if current_time - st.session_state.last_update > 0.5:  # Update every 500ms
        st.session_state.game.update()
        st.session_state.last_update = current_time
    
    # Draw game
    try:
        game_canvas.image(st.session_state.game.draw())
    except Exception as e:
        st.error(f"Drawing error: {str(e)}")

if __name__ == "__main__":
    main() 
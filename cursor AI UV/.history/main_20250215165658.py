import streamlit as st
import numpy as np
import pygame

# Initialize pygame
pygame.init()

# Constants
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * GRID_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

class SimpleGame:
    def __init__(self):
        # Create pygame surface
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        # Initialize block position
        self.block_x = GRID_WIDTH // 2
        self.block_y = 0
        # Initialize grid
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.score = 0
        
    def move_left(self):
        if self.block_x > 0:
            self.block_x -= 1
            
    def move_right(self):
        if self.block_x < GRID_WIDTH - 1:
            self.block_x += 1
            
    def move_down(self):
        if self.block_y < GRID_HEIGHT - 1:
            self.block_y += 1
            return True
        return False
        
    def draw(self):
        # Fill background
        self.surface.fill((0, 0, 0))
        
        # Draw grid
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                pygame.draw.rect(
                    self.surface,
                    (50, 50, 50),
                    (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    1
                )
                
        # Draw block
        pygame.draw.rect(
            self.surface,
            (255, 0, 0),
            (self.block_x * BLOCK_SIZE, 
             self.block_y * BLOCK_SIZE,
             BLOCK_SIZE - 2, 
             BLOCK_SIZE - 2)
        )
        
        # Convert to numpy array
        view = pygame.surfarray.array3d(self.surface)
        return np.transpose(view, [1, 0, 2])

def main():
    st.title("Simple Block Game")
    
    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = SimpleGame()
    
    # Create layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Game board
        game_canvas = st.empty()
    
    with col2:
        # Controls
        st.write("Controls")
        
        cols = st.columns(3)
        with cols[0]:
            if st.button("⬅️"):
                st.session_state.game.move_left()
        with cols[1]:
            if st.button("⬇️"):
                st.session_state.game.move_down()
        with cols[2]:
            if st.button("➡️"):
                st.session_state.game.move_right()
                
        if st.button("Reset"):
            st.session_state.game = SimpleGame()
    
    # Draw game
    try:
        game_canvas.image(st.session_state.game.draw())
    except Exception as e:
        st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
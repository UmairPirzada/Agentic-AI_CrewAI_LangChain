import streamlit as st
import numpy as np
import pygame

# Initialize Pygame
pygame.init()

# Constants
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * GRID_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

class Game:
    def __init__(self):
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.reset()
    
    def reset(self):
        self.block_x = GRID_WIDTH // 2
        self.block_y = 0
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
        # Clear screen
        self.surface.fill((0, 0, 0))
        
        # Draw grid
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                pygame.draw.rect(
                    self.surface,
                    (40, 40, 40),
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
        
        # Convert surface to numpy array
        return np.transpose(
            pygame.surfarray.array3d(self.surface),
            (1, 0, 2)
        )

def main():
    # Set up Streamlit page
    st.set_page_config(
        page_title="Tetris Test",
        layout="wide"
    )
    
    # Title
    st.title("Tetris Test")
    
    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = Game()
    
    # Create two columns
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Game display
        placeholder = st.empty()
    
    with col2:
        # Controls
        st.subheader("Controls")
        
        col_left, col_right = st.columns(2)
        
        with col_left:
            if st.button("⬅️"):
                st.session_state.game.move_left()
        
        with col_right:
            if st.button("➡️"):
                st.session_state.game.move_right()
        
        if st.button("⬇️"):
            st.session_state.game.move_down()
        
        if st.button("Reset"):
            st.session_state.game.reset()
        
        st.write(f"Score: {st.session_state.game.score}")
    
    # Update game display
    try:
        game_display = st.session_state.game.draw()
        placeholder.image(game_display)
    except Exception as e:
        st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 
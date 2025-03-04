import streamlit as st
import numpy as np

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30

def create_game_board():
    # Create a black background with a grid
    board = np.zeros((GRID_HEIGHT * CELL_SIZE, GRID_WIDTH * CELL_SIZE, 3), dtype=np.uint8)
    
    # Draw grid lines
    for x in range(0, GRID_WIDTH * CELL_SIZE, CELL_SIZE):
        board[:, x] = [50, 50, 50]
    for y in range(0, GRID_HEIGHT * CELL_SIZE, CELL_SIZE):
        board[y, :] = [50, 50, 50]
    
    return board

class Game:
    def __init__(self):
        self.board = create_game_board()
        self.block_x = GRID_WIDTH // 2
        self.block_y = 0
        
    def move_left(self):
        if self.block_x > 0:
            self.block_x -= 1
            
    def move_right(self):
        if self.block_x < GRID_WIDTH - 1:
            self.block_x += 1
            
    def move_down(self):
        if self.block_y < GRID_HEIGHT - 1:
            self.block_y += 1
            
    def draw(self):
        # Create a copy of the board
        display = self.board.copy()
        
        # Draw the block
        x = self.block_x * CELL_SIZE
        y = self.block_y * CELL_SIZE
        display[y:y+CELL_SIZE-1, x:x+CELL_SIZE-1] = [255, 0, 0]
        
        return display

def main():
    st.set_page_config(page_title="Simple Game", layout="wide")
    st.title("Simple Block Game")
    
    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = Game()
    
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
            st.session_state.game = Game()
    
    # Draw game
    game_canvas.image(st.session_state.game.draw())

if __name__ == "__main__":
    main() 
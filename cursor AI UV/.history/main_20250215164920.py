import streamlit as st
import pygame
import numpy as np
from src.constants import (
    COLORS, SHAPES, BLOCK_SIZE, 
    BOARD_WIDTH, BOARD_HEIGHT,
    WINDOW_WIDTH, WINDOW_HEIGHT
)

# Set up page configuration
st.set_page_config(
    page_title="UV Tetris",
    layout="wide"
)

# Add custom CSS for better appearance
st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
        }
        .game-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

# JavaScript for keyboard controls
js_code = """
<script>
document.addEventListener('keydown', function(e) {
    const key = e.key;
    if (['ArrowLeft', 'ArrowRight', 'ArrowDown', 'ArrowUp', ' '].includes(key)) {
        e.preventDefault();
        const data = {
            type: "keydown",
            key: key
        };
        window.parent.postMessage(data, "*");
    }
});
</script>
"""

def handle_keyboard_input():
    if 'keyboard_input' not in st.session_state:
        st.session_state.keyboard_input = None
    
    # Get keyboard input from JavaScript
    st.session_state.keyboard_input = None
    html(js_code, height=0)

class TetrisGame:
    def __init__(self):
        self.board = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_piece = self.new_piece()
        self.score = 0
        self.game_over = False
        
        # Initialize Pygame
        pygame.init()
        self.surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    def new_piece(self):
        import random
        shape_name = random.choice(list(SHAPES.keys()))
        return {
            'shape': SHAPES[shape_name],
            'color': COLORS[shape_name],
            'x': BOARD_WIDTH // 2 - 1,
            'y': 0
        }
    
    def draw(self):
        # Fill background
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
        
        # Convert surface to numpy array for Streamlit
        view = pygame.surfarray.array3d(self.surface)
        return np.transpose(view, [1, 0, 2])
    
    def update(self):
        if self.game_over:
            return
            
        # Move piece down
        self.current_piece['y'] += 1
        
        # Check if piece needs to be placed
        if self.check_collision():
            self.current_piece['y'] -= 1
            self.place_piece()
            self.current_piece = self.new_piece()
            if self.check_collision():
                self.game_over = True
    
    def check_collision(self):
        for x, y in self.current_piece['shape']:
            new_x = self.current_piece['x'] + x
            new_y = self.current_piece['y'] + y
            
            if (new_y >= BOARD_HEIGHT or 
                new_x < 0 or 
                new_x >= BOARD_WIDTH or 
                (new_y >= 0 and self.board[new_y][new_x])):
                return True
        return False
    
    def place_piece(self):
        for x, y in self.current_piece['shape']:
            board_y = self.current_piece['y'] + y
            board_x = self.current_piece['x'] + x
            if board_y >= 0:
                self.board[board_y][board_x] = self.current_piece['color']
        
        # Check for completed lines
        self.clear_lines()
    
    def clear_lines(self):
        lines_cleared = 0
        y = BOARD_HEIGHT - 1
        while y >= 0:
            if all(cell is not None for cell in self.board[y]):
                self.board.pop(y)
                self.board.insert(0, [None] * BOARD_WIDTH)
                lines_cleared += 1
            else:
                y -= 1
        self.score += lines_cleared * 100

def main():
    st.title("Simple Tetris")
    
    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = TetrisGame()
        st.session_state.last_update = 0
    
    # Create layout
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Game board
        game_canvas = st.empty()
    
    with col2:
        # Score and controls
        st.write(f"Score: {st.session_state.game.score}")
        
        if st.button("New Game"):
            st.session_state.game = TetrisGame()
    
    # Game loop
    import time
    current_time = time.time()
    if current_time - st.session_state.last_update > 0.5:  # Update every 500ms
        st.session_state.game.update()
        st.session_state.last_update = current_time
    
    # Draw game
    game_canvas.image(st.session_state.game.draw())

if __name__ == "__main__":
    main() 
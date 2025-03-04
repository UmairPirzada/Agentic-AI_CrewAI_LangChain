import streamlit as st
from src.game import TetrisGame
import time
import pygame
from streamlit.components.v1 import html

st.set_page_config(
    page_title="UV Tetris",
    layout="wide"
)

# JavaScript for keyboard controls
js_code = """
<script>
document.addEventListener('keydown', function(e) {
    const key = e.key;
    if (['ArrowLeft', 'ArrowRight', 'ArrowDown', 'ArrowUp', ' '].includes(key)) {
        e.preventDefault();
        window.parent.postMessage({
            type: "keydown",
            key: key
        }, "*");
    }
});
</script>
"""

def main():
    st.title("UV Tetris Game")
    
    # Initialize game state
    if 'game' not in st.session_state:
        st.session_state.game = TetrisGame()
        st.session_state.score = 0
        st.session_state.game_over = False
        st.session_state.last_update = time.time()

    # Create two columns
    col1, col2 = st.columns([3, 1])

    with col1:
        # Game board display
        game_canvas = st.empty()
        # Add keyboard listener
        html(js_code, height=0)
    
    with col2:
        # Game controls and info
        st.subheader("Score")
        score_display = st.empty()
        score_display.text(f"{st.session_state.score}")
        
        st.subheader("Controls")
        st.write("← : Move Left")
        st.write("→ : Move Right")
        st.write("↓ : Move Down")
        st.write("↑ : Rotate")
        st.write("Space : Hard Drop")
        
        if st.button("New Game"):
            st.session_state.game = TetrisGame()
            st.session_state.score = 0
            st.session_state.game_over = False

    # Game loop
    if not st.session_state.game_over:
        current_time = time.time()
        if current_time - st.session_state.last_update > 0.5:  # Update every 500ms
            st.session_state.game.update()
            st.session_state.last_update = current_time
        
        # Display game board
        game_canvas.image(st.session_state.game.draw_board())
        
        # Update score
        score_display.text(f"{st.session_state.game.score}")

if __name__ == "__main__":
    main() 
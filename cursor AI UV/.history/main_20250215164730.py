import streamlit as st
from src.game import TetrisGame
import time
from streamlit.components.v1 import html

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
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        game_canvas = st.empty()
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Handle keyboard input
        handle_keyboard_input()
    
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

        if st.button("Move Left"):
            st.session_state.game.move(-1, 0)
        if st.button("Move Right"):
            st.session_state.game.move(1, 0)
        if st.button("Rotate"):
            st.session_state.game.rotate()
        if st.button("Drop"):
            st.session_state.game.hard_drop()

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
import streamlit as st
from src.game import TetrisGame
import time

st.set_page_config(
    page_title="UV Tetris",
    layout="wide"
)

def main():
    st.title("UV Tetris Game")
    
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
    
    with col2:
        # Game controls and info
        st.subheader("Score")
        score_display = st.empty()
        score_display.text(f"{st.session_state.score}")
        
        st.subheader("Controls")
        st.write("Use keyboard controls:")
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
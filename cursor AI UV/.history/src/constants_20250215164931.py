# Colors for different tetrominos (using RGB format for pygame)
COLORS = {
    'I': (0, 240, 240),  # Cyan
    'O': (240, 240, 0),  # Yellow
    'T': (160, 0, 240),  # Purple
    'S': (0, 240, 0),    # Green
    'Z': (240, 0, 0),    # Red
    'J': (0, 0, 240),    # Blue
    'L': (240, 160, 0)   # Orange
}

# Game constants
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
GAME_SPEED = 500  # milliseconds

# Window dimensions
WINDOW_WIDTH = BLOCK_SIZE * BOARD_WIDTH
WINDOW_HEIGHT = BLOCK_SIZE * BOARD_HEIGHT

# Tetromino shapes
SHAPES = {
    'I': [(0, 0), (0, 1), (0, 2), (0, 3)],
    'O': [(0, 0), (0, 1), (1, 0), (1, 1)],
    'T': [(0, 1), (1, 0), (1, 1), (1, 2)],
    'S': [(0, 1), (0, 2), (1, 0), (1, 1)],
    'Z': [(0, 0), (0, 1), (1, 1), (1, 2)],
    'J': [(0, 0), (1, 0), (1, 1), (1, 2)],
    'L': [(0, 2), (1, 0), (1, 1), (1, 2)]
} 
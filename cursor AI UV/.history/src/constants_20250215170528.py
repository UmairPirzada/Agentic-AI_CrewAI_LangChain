# Game dimensions
CELL_SIZE = 25  # Smaller blocks for better visuals
GRID_WIDTH = 10
GRID_HEIGHT = 20
PREVIEW_SIZE = 4  # For next piece preview

# Colors (RGB)
COLORS = {
    'I': (0, 240, 240),   # Cyan
    'O': (240, 240, 0),   # Yellow
    'T': (160, 0, 240),   # Purple
    'S': (0, 240, 0),     # Green
    'Z': (240, 0, 0),     # Red
    'J': (0, 0, 240),     # Blue
    'L': (240, 160, 0),   # Orange
    'GRID': (50, 50, 50), # Grid lines
    'BG': (0, 0, 0),      # Background
}

# Tetromino shapes with better rotation points
SHAPES = {
    'I': [(0, 1), (-1, 1), (1, 1), (2, 1)],  # Horizontal I as base
    'O': [(0, 0), (1, 0), (0, 1), (1, 1)],   # O doesn't rotate
    'T': [(0, 0), (-1, 0), (1, 0), (0, 1)],  # T pointing up
    'S': [(0, 0), (-1, 0), (0, 1), (1, 1)],  # S shape
    'Z': [(0, 0), (1, 0), (0, 1), (-1, 1)],  # Z shape
    'J': [(0, 0), (-1, 0), (1, 0), (-1, 1)], # J pointing up
    'L': [(0, 0), (-1, 0), (1, 0), (1, 1)],  # L pointing up
}

# Game speeds (in milliseconds)
INITIAL_SPEED = 800
SPEED_INCREASE = 50
MIN_SPEED = 100

# Scoring system
POINTS = {
    'SINGLE': 100,    # Single line clear
    'DOUBLE': 300,    # Double line clear
    'TRIPLE': 500,    # Triple line clear
    'TETRIS': 800,    # Four lines clear
    'SOFT_DROP': 1,   # Points per cell for soft drop
    'HARD_DROP': 2,   # Points per cell for hard drop
}

# Level system
LINES_PER_LEVEL = 10

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
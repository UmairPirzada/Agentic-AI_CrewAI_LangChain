import random
from .constants import SHAPES, COLORS

class Tetromino:
    def __init__(self):
        self.shape_name = random.choice(list(SHAPES.keys()))
        self.shape = SHAPES[self.shape_name].copy()
        self.color = COLORS[self.shape_name]
        self.x = 4  # Starting position
        self.y = 0
        self.rotation = 0

    def rotate(self, board, clockwise=True):
        """Rotate the tetromino with wall kicks"""
        old_shape = self.shape.copy()
        old_x = self.x
        
        # Rotate the piece
        new_shape = []
        for x, y in self.shape:
            if clockwise:
                new_shape.append((-y, x))
            else:
                new_shape.append((y, -x))
        self.shape = new_shape

        # Wall kick positions to try
        kicks = [(0, 0), (-1, 0), (1, 0), (0, -1)]
        if self.shape_name == 'I':
            kicks.extend([(-2, 0), (2, 0)])

        # Try wall kicks
        for kick_x, kick_y in kicks:
            self.x += kick_x
            self.y += kick_y
            if board.is_valid_move(self):
                return True
            self.x -= kick_x
            self.y -= kick_y

        # If no wall kick worked, restore old position
        self.shape = old_shape
        self.x = old_x
        return False

    def get_positions(self):
        """Get absolute positions of all blocks"""
        return [(self.x + x, self.y + y) for x, y in self.shape]

    def move(self, dx, dy):
        """Move the tetromino"""
        self.x += dx
        self.y += dy

    def get_ghost_position(self, board):
        """Get the position where the piece would land"""
        ghost_y = self.y
        while True:
            ghost_y += 1
            ghost_positions = [(self.x + x, ghost_y + y) for x, y in self.shape]
            if not self._is_valid_position(ghost_positions, board):
                return ghost_y - 1
                
    def _is_valid_position(self, positions, board):
        """Helper method to check position validity"""
        for x, y in positions:
            if not (0 <= x < board.width and y < board.height):
                return False
            if y >= 0 and board.grid[y][x] is not None:
                return False
        return True 
import numpy as np
from .constants import GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, COLORS

class Board:
    def __init__(self):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.current_piece = None
        self.next_piece = None
        
    def is_valid_move(self, piece):
        """Check if piece position is valid"""
        for x, y in piece.get_positions():
            if not (0 <= x < GRID_WIDTH and y < GRID_HEIGHT):
                return False
            if y >= 0 and self.grid[y][x] is not None:
                return False
        return True
    
    def place_piece(self, piece):
        """Place the piece on the board"""
        for x, y in piece.get_positions():
            if y >= 0:
                self.grid[y][x] = piece.color
    
    def clear_lines(self):
        """Clear completed lines and return number of lines cleared"""
        lines_cleared = 0
        y = GRID_HEIGHT - 1
        while y >= 0:
            if all(cell is not None for cell in self.grid[y]):
                self.grid.pop(y)
                self.grid.insert(0, [None] * GRID_WIDTH)
                lines_cleared += 1
            else:
                y -= 1
        return lines_cleared

    def draw(self):
        """Draw the board state with improved visuals"""
        # Create empty board with background
        board = np.full((self.height * CELL_SIZE, self.width * CELL_SIZE, 3), 
                       COLORS['BG'], dtype=np.uint8)
        
        # Draw grid lines
        for x in range(0, self.width * CELL_SIZE, CELL_SIZE):
            board[:, x] = COLORS['GRID']
        for y in range(0, self.height * CELL_SIZE, CELL_SIZE):
            board[y, :] = COLORS['GRID']
        
        # Draw ghost piece
        if self.current_piece:
            ghost_y = self.current_piece.get_ghost_position(self)
            ghost_positions = [(x, ghost_y) for x, _ in self.current_piece.get_positions()]
            for x, y in ghost_positions:
                if 0 <= y < self.height:
                    self._draw_block(board, x, y, self.current_piece.color, ghost=True)
        
        # Draw placed pieces
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x]:
                    self._draw_block(board, x, y, self.grid[y][x])
        
        # Draw current piece
        if self.current_piece:
            for x, y in self.current_piece.get_positions():
                if y >= 0:
                    self._draw_block(board, x, y, self.current_piece.color)
        
        return board
    
    def _draw_block(self, board, x, y, color, ghost=False):
        """Draw a single block with shading"""
        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        x2 = x1 + CELL_SIZE - 1
        y2 = y1 + CELL_SIZE - 1
        
        if ghost:
            # Draw ghost piece with transparency effect
            board[y1:y2, x1:x2] = [c // 4 for c in color]
            return
            
        # Main block color
        board[y1:y2, x1:x2] = color
        
        # Light edge (top, left)
        board[y1:y1+2, x1:x2] = [min(c + 50, 255) for c in color]
        board[y1:y2, x1:x1+2] = [min(c + 50, 255) for c in color]
        
        # Dark edge (bottom, right)
        board[y2-2:y2, x1:x2] = [max(c - 50, 0) for c in color]
        board[y1:y2, x2-2:x2] = [max(c - 50, 0) for c in color] 
import numpy as np
from .constants import GRID_WIDTH, GRID_HEIGHT, CELL_SIZE

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = None
        
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
        """Draw the board state"""
        # Create empty board
        board = np.zeros((GRID_HEIGHT * CELL_SIZE, GRID_WIDTH * CELL_SIZE, 3), dtype=np.uint8)
        
        # Draw grid lines
        for x in range(0, GRID_WIDTH * CELL_SIZE, CELL_SIZE):
            board[:, x] = [40, 40, 40]
        for y in range(0, GRID_HEIGHT * CELL_SIZE, CELL_SIZE):
            board[y, :] = [40, 40, 40]
        
        # Draw placed pieces
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    self._draw_block(board, x, y, self.grid[y][x])
        
        # Draw current piece
        if self.current_piece:
            for x, y in self.current_piece.get_positions():
                if y >= 0:
                    self._draw_block(board, x, y, self.current_piece.color)
        
        return board
    
    def _draw_block(self, board, x, y, color):
        """Draw a single block"""
        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        board[y1:y1+CELL_SIZE-1, x1:x1+CELL_SIZE-1] = color 
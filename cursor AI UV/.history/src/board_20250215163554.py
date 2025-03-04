from .constants import BOARD_WIDTH, BOARD_HEIGHT

class Board:
    def __init__(self):
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]

    def is_valid_move(self, tetromino):
        """Check if the tetromino's current position is valid"""
        for x, y in tetromino.get_positions():
            if not (0 <= x < self.width and y < self.height):
                return False
            if y >= 0 and self.grid[y][x] is not None:
                return False
        return True

    def place_tetromino(self, tetromino):
        """Place the tetromino on the board"""
        for x, y in tetromino.get_positions():
            if y >= 0:
                self.grid[y][x] = tetromino.color

    def clear_lines(self):
        """Clear completed lines and return the number of lines cleared"""
        lines_cleared = 0
        y = self.height - 1
        while y >= 0:
            if all(cell is not None for cell in self.grid[y]):
                self.grid.pop(y)
                self.grid.insert(0, [None] * self.width)
                lines_cleared += 1
            else:
                y -= 1
        return lines_cleared 
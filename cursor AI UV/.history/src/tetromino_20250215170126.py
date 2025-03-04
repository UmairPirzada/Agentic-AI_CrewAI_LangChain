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

    def rotate(self):
        """Rotate the tetromino clockwise"""
        new_shape = []
        for x, y in self.shape:
            new_x = -y
            new_y = x
            new_shape.append((new_x, new_y))
        self.shape = new_shape

    def get_positions(self):
        """Get absolute positions of all blocks"""
        return [(self.x + x, self.y + y) for x, y in self.shape]

    def move(self, dx, dy):
        """Move the tetromino"""
        self.x += dx
        self.y += dy 
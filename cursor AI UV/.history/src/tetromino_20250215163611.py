import random
from .constants import SHAPES, COLORS

class Tetromino:
    def __init__(self):
        self.shape_name = random.choice(list('IOTSZJL'))
        self.shape = self._get_shape()
        self.color = COLORS[self.shape_name]
        self.x = 4
        self.y = 0
        self.rotation = 0

    def _get_shape(self):
        """Get the shape coordinates based on shape name"""
        shapes = {
            'I': [(0, 0), (0, 1), (0, 2), (0, 3)],
            'O': [(0, 0), (0, 1), (1, 0), (1, 1)],
            'T': [(0, 1), (1, 0), (1, 1), (1, 2)],
            'S': [(0, 1), (0, 2), (1, 0), (1, 1)],
            'Z': [(0, 0), (0, 1), (1, 1), (1, 2)],
            'J': [(0, 0), (1, 0), (1, 1), (1, 2)],
            'L': [(0, 2), (1, 0), (1, 1), (1, 2)]
        }
        return shapes[self.shape_name]

    def rotate(self):
        """Rotate the tetromino 90 degrees clockwise"""
        new_shape = []
        for x, y in self.shape:
            new_x = -y
            new_y = x
            new_shape.append((new_x, new_y))
        self.shape = new_shape

    def move(self, dx, dy):
        """Move the tetromino by the given delta x and y"""
        self.x += dx
        self.y += dy

    def get_positions(self):
        """Get the absolute positions of all blocks in the tetromino"""
        return [(self.x + x, self.y + y) for x, y in self.shape] 
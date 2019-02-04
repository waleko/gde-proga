import tkinter as tk
import random
from MazeGenerator import generate_maze


class Board:
    def __init__(self, root, field_size, one_tile_size):
        if not isinstance(field_size, tuple):
            print('Field size tuple is not a tuple!')
            exit(1)
            return
        w = field_size[0]
        h = field_size[1]
        if (not isinstance(w, int)) or (not isinstance(h, int)):
            print('Field size parameters are not integers!')
            exit(2)
        if w <= 0 or h <= 0:
            print('Field size parameters are invalid integers!')
            exit(3)
        self.w = w
        self.h = h
        self.field_size = field_size

        self.canvas = tk.Canvas(root, width=w * one_tile_size, height=h * one_tile_size, bg='#FFCCCC')
        self.canvas.pack()

        start_position = (random.randint(0, w - 1), random.randint(0, h - 1))

        self.x = start_position[0]
        self.y = start_position[1]
        self.maze, self.end_position = generate_maze(w, h, self.x, self.y)
        self.start_position = start_position

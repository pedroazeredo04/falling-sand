from src.grid import Grid
from src.grid import Vector2D
from src.grid import CellType
import random


class Simulation:
    def __init__(self, grid: Grid):
        self.grid_ = grid
        self.changes_ = []


    def step(self):
        for x in range(self.grid_.cols_):
            for y in range(self.grid_.rows_):
                pos = Vector2D(self.grid_.cols_ - x, self.grid_.rows_ - y)

                if self.grid_.get_cell(pos) == CellType.SAND:
                    delta_y = Vector2D(0, 1)
                    delta_x = Vector2D(1, 0)

                    is_left = not not random.getrandbits(1)

                    if not is_left:
                        delta_x = -1 * delta_x

                    if self.grid_.get_cell(pos + delta_y) == CellType.VOID:
                        self.grid_.place_void(pos)
                        self.grid_.place_sand(pos + delta_y)
                    elif self.grid_.get_cell(pos + delta_y + delta_x) == CellType.VOID:
                        self.grid_.place_void(pos)
                        self.grid_.place_sand(pos + delta_y + delta_x)

                    elif self.grid_.get_cell(pos + delta_y - delta_x) == CellType.VOID:
                        self.grid_.place_void(pos)
                        self.grid_.place_sand(pos + delta_y - delta_x)

from src.grid import Grid
from src.grid import Vector2D
from src.grid import CellType
import random


class Simulation:
    def __init__(self, grid: Grid):
        self.grid_ = grid
        self.changes_ = []

    def move_cell(self, cell_origin: Vector2D, cell_destiny: Vector2D):
        self.changes_.append((cell_origin, cell_destiny))

    def commit_changes(self):
        # Filter out invalid moves (destinations not empty at the moment of decision)
        valid_moves = []
        for origin, dest in self.changes_:
            if self.grid_.get_cell(dest) == CellType.VOID:
                valid_moves.append((origin, dest))

        # Randomize order to avoid directional bias
        random.shuffle(valid_moves)

        # Apply all moves now
        for origin, dest in valid_moves:
            cell_type = self.grid_.get_cell(origin)
            if (
                cell_type != CellType.VOID
                and self.grid_.get_cell(dest) == CellType.VOID
            ):
                self.grid_.place(cell_type, dest)
                self.grid_.place(CellType.VOID, origin)

        self.changes_.clear()

    def step(self):
        for x in range(self.grid_.cols_):
            for y in reversed(range(self.grid_.rows_)):
                pos = Vector2D(x, y)

                if self.grid_.get_cell(pos) == CellType.SAND:
                    delta_y = Vector2D(0, 1)
                    right = Vector2D(1, 0)
                    left = Vector2D(-1, 0)
                    lateral = right if random.getrandbits(1) else left

                    if self.grid_.is_empty(pos + delta_y):
                        self.move_cell(pos, pos + delta_y)
                    elif self.grid_.is_empty(
                        pos + delta_y + lateral
                    ) and self.grid_.is_empty(pos + lateral):
                        self.move_cell(pos, pos + delta_y + lateral)
                    elif self.grid_.is_empty(
                        pos + delta_y - lateral
                    ) and self.grid_.is_empty(pos - lateral):
                        self.move_cell(pos, pos + delta_y - lateral)

                if self.grid_.get_cell(pos) == CellType.WATER:
                    delta_y = Vector2D(0, 1)
                    right = Vector2D(1, 0)
                    left = Vector2D(-1, 0)
                    lateral = right if random.getrandbits(1) else left

                    if self.grid_.is_empty(pos + delta_y):
                        self.move_cell(pos, pos + delta_y)
                    elif self.grid_.is_empty(pos + lateral):
                        self.move_cell(pos, pos + lateral)
                    elif self.grid_.is_empty(pos - lateral):
                        self.move_cell(pos, pos - lateral)
        self.commit_changes()

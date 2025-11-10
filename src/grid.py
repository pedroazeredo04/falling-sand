from enum import Enum


# Vector class
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # operators overloading
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __rmul__(self, num):
        return Vector2D(num * self.x, num * self.y)

    # turn Vector2D into a tuple
    def tuple(self):
        return (self.x, self.y)

    def __eq__(self, o):
        return isinstance(o, Vector2D) and self.x == o.x and self.y == o.y

    def __hash__(self):
        return hash((self.x, self.y))


class CellType(Enum):
    VOID = 0
    SAND = 1
    WALL = 2
    WATER = 3


class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows_ = rows
        self.cols_ = cols
        self.grid_ = [[CellType.VOID for _ in range(cols)] for _ in range(rows)]

    def in_bounds(self, cell: Vector2D) -> bool:
        return 0 <= cell.x < self.cols_ and 0 <= cell.y < self.rows_

    def place(self, cell_type: CellType, cell: Vector2D):
        self.grid_[cell.y][cell.x] = cell_type

    def idx_to_cell(self, idx: int) -> Vector2D:
        cell_x = idx % self.cols_
        cell_y = idx // self.cols_
        return Vector2D(cell_x, cell_y)

    def get_cell(self, cell: Vector2D) -> CellType:
        if not self.in_bounds(cell):
            return CellType.WALL

        return self.grid_[cell.y][cell.x]

    def get_cell_index(self, cell: Vector2D) -> int:
        if not self.in_bounds(cell):
            return -1

        return cell.x + cell.y * self.cols_

    def is_empty(self, cell: Vector2D) -> bool:
        return self.get_cell(cell) == CellType.VOID

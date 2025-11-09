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


class CellType(Enum):
    VOID = 0
    SAND = 1
    WALL = 2


class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows_ = rows
        self.cols_ = cols
        self.grid_ = [[CellType.VOID for _ in range(cols)] for _ in range(rows)]

    def place_sand(self, cell: Vector2D):
        self.grid_[cell.y][cell.x] = CellType.SAND

    def place_void(self, cell: Vector2D):
        self.grid_[cell.y][cell.x] = CellType.VOID

    def place_wall(self, cell: Vector2D):
        self.grid_[cell.y][cell.x] = CellType.WALL

    def get_cell(self, cell:Vector2D) -> CellType:
        if cell.y < 0 or cell.y >= self.rows_:
            return CellType.WALL
        
        if cell.x < 0 or cell.x >= self.cols_:
            return CellType.WALL

        return self.grid_[cell.y][cell.x]

    def get_cell_index(self, cell: Vector2D) -> int:
        if cell.y < 0 or cell.y >= self.rows_:
            return -1
        
        if cell.x < 0 or cell.x >= self.cols_:
            return -1

        return cell.x + cell.y * self.cols_

    def is_empty(self, cell: Vector2D) -> bool:
        return self.grid_[cell.y][cell.x] == CellType.VOID

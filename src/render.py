import pygame

from src.grid import Grid
from src.grid import Vector2D
from src.grid import CellType
from src.sim import Simulation


color_dict = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "sand": (233, 189, 134),
    "water": (0, 21, 234),
    "wall": (0, 0, 0,),
}


class Render:
    def __init__(self, window_w: int, window_h: int, pixels_per_cell: int):
        self.window_w_ = window_w
        self.window_h_ = window_h
        self.pixels_per_cell_ = pixels_per_cell

        self.rows = int(window_h / pixels_per_cell)
        self.cols = int(window_w / pixels_per_cell)
        self.grid = Grid(self.rows, self.cols)

        self.sim = Simulation(self.grid)

    def init_screen(self, background_color):
        screen_size = (self.window_w_, self.window_h_)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Random Walk")
        self.screen.fill(background_color)

    def run_sim(self):
        self.running = True
        self.pause = False
        while self.running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = True if not self.pause else False

            pressed_keys = pygame.key.get_pressed()
            
            if pressed_keys[pygame.K_w]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                cell_vec = self.get_mouse_cell(mouse_x, mouse_y)
                self.grid.place(CellType.WATER, cell_vec)

            if pressed_keys[pygame.K_s]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                cell_vec = self.get_mouse_cell(mouse_x, mouse_y)
                self.grid.place(CellType.SAND, cell_vec)

            if pressed_keys[pygame.K_b]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                cell_vec = self.get_mouse_cell(mouse_x, mouse_y)
                self.grid.place(CellType.WALL, cell_vec)

            if pressed_keys[pygame.K_BACKSPACE]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                cell_vec = self.get_mouse_cell(mouse_x, mouse_y)
                self.grid.place(CellType.VOID, cell_vec)

            if pressed_keys[pygame.K_ESCAPE]:
                self.grid = Grid(self.rows, self.cols)
                self.sim = Simulation(self.grid)


            if not self.pause:
                self.sim.step()
                if pygame.mouse.get_pressed()[0]:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    cell_vec = self.get_mouse_cell(mouse_x, mouse_y)
                    self.grid.place(CellType.SAND, cell_vec)

            self.screen.fill(color_dict["white"])
            self.draw_grid()
            self.draw_squares()
            pygame.display.flip()

    def draw_squares(self):
        for i in range(self.cols + 1):
            x_coord = self.pixels_per_cell_ * i
            pygame.draw.line(
                self.screen,
                color_dict["black"],
                (x_coord, 0),
                (x_coord, self.window_h_),
            )

        for j in range(self.rows + 1):
            y_coord = self.pixels_per_cell_ * j
            pygame.draw.line(
                self.screen,
                color_dict["black"],
                (0, y_coord),
                (self.window_w_, y_coord),
            )

    def draw_grid(self):
        for y in range(self.rows):
            for x in range(self.cols):
                if self.grid.grid_[y][x] == CellType.SAND:
                    rec = pygame.Rect(
                        x * self.pixels_per_cell_,
                        y * self.pixels_per_cell_,
                        self.pixels_per_cell_,
                        self.pixels_per_cell_,
                    )
                    pygame.draw.rect(self.screen, color_dict["sand"], rec, 5)

                if self.grid.grid_[y][x] == CellType.WATER:
                    rec = pygame.Rect(
                        x * self.pixels_per_cell_,
                        y * self.pixels_per_cell_,
                        self.pixels_per_cell_,
                        self.pixels_per_cell_,
                    )
                    pygame.draw.rect(self.screen, color_dict["water"], rec, 5)

                if self.grid.grid_[y][x] == CellType.WALL:
                    rec = pygame.Rect(
                        x * self.pixels_per_cell_,
                        y * self.pixels_per_cell_,
                        self.pixels_per_cell_,
                        self.pixels_per_cell_,
                    )
                    pygame.draw.rect(self.screen, color_dict["wall"], rec, 5)

    def get_mouse_cell(self, mouse_x: float, mouse_y: float) -> Vector2D:
        cell_x = int(mouse_x / self.pixels_per_cell_)
        cell_y = int(mouse_y / self.pixels_per_cell_)
        return Vector2D(cell_x, cell_y)

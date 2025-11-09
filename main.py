from src.render import Render
from src.grid import Grid
from src.grid import Vector2D


def main():
    screen_size = 1.5 * Vector2D(1000, 500)
    pixels_per_cell = 10
    render = Render(screen_size.x, screen_size.y, pixels_per_cell)
    background_color = (255, 255, 255)

    render.init_screen(background_color)
    render.draw_squares()
    render.run_sim()


if __name__ == "__main__":
    main()

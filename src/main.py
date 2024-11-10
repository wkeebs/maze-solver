from window import Window
from draw import Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    
    c = Cell(100, 100, 200, 200, win)
    c.has_right_wall = False
    c.draw()
    
    win.wait_for_close()


if __name__ == "__main__":
    main()

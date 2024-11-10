from window import Window
from draw import Line, Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    
    m = Maze(50, 50, 4, 4, 100, 100, win)
    m.create_cells()
    
    win.wait_for_close()


if __name__ == "__main__":
    main()

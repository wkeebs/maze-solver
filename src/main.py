from window import Window
from draw import Line, Point
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)
    
    m = Maze(20, 20, 10, 10, 30, 30, win)
    m.solve()
    
    win.wait_for_close()


if __name__ == "__main__":
    main()

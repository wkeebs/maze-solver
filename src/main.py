from window import Window
from draw import Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    
    c1 = Cell(100, 100, 200, 200, win)
    c1.has_right_wall = False
    c1.draw()
    
    c2 = Cell(400, 100, 500, 200, win)
    c2.has_left_wall = False
    c2.draw()
    
    c1.draw_move(c2)
    
    win.wait_for_close()


if __name__ == "__main__":
    main()

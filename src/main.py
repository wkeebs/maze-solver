from window import Window
from draw import Line, Point


def main():
    win = Window(800, 600)
    
    line = Line(Point(200, 300), Point(300, 400))
    win.draw_line(line, "red")
    
    win.wait_for_close()


if __name__ == "__main__":
    main()

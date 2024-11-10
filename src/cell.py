from window import Window
from draw import Point, Line
from typing import Self


class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, win: Window):
        """
        : @summary :
        Represents a maze cell. Has 4 potential walls and a location.
        ___________________

        : @args :
            * x1 (int): left
            * y1 (int): top
            * x2 (int): right
            * y2 (int): bottom
            * win (Window): the window it is in
        ___________________
        """
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win

    def draw(self):
        """
        : @summary :
        Draws the cell in the window.
        ___________________
        """
        top_left = Point(self.__x1, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        top_right = Point(self.__x2, self.__y1)
        bottom_right = Point(self.__x2, self.__y2)

        lines = []
        if self.has_left_wall:
            lines.append(Line(top_left, bottom_left))
        if self.has_top_wall:
            lines.append(Line(top_left, top_right))
        if self.has_right_wall:
            lines.append(Line(top_right, bottom_right))
        if self.has_bottom_wall:
            lines.append(Line(bottom_left, bottom_right))

        for line in lines:
            self.__win.draw_line(line)

    def draw_move(self, other: Self, undo: bool = False):
        """
        : @summary :
        Draws a line from the center of the cell to the center of another.
        ___________________

        : @args :
            * other (Self): the other cell
            * undo (bool): whether the move is an "undo" move or not
        ___________________
        """
        self_middle = Point(self.__x1 + self.__x2 // 2,
                            self.__y1 + self.__y2 // 2)
        other_middle = Point(other.__x1 + other.__x2 // 2,
                             other.__y1 + other.__y2 // 2)
        colour = "gray" if undo else "red"
        connecting_line = Line(self_middle, other_middle)
        self.__win.draw_line(connecting_line, colour)
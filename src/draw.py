from tkinter import Canvas


class Point:
    def __init__(self, x: int, y: int):
        """
        : @summary :
        Represents a single point on the canvas.
        ___________________

        : @args :
            * x (int): the x coordinate (horizontal)
            * y (int): the y coordinate (vertical)
        ___________________
        """
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1: Point, point2: Point):
        """
        : @summary :
        Represents a line on the canvas, between two points.
        ___________________

        : @args :
            * point1 (Point): the first endpoint
            * point2 (Point): the second endpoint
        """
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas: Canvas, fill_color: str = "black"):
        """
        : @summary :
        Renders the line on a canvas.
        ___________________

        : @args :
            * canvas (Canvas): the canvas to render on
            * fill_color (str): the colour of the line
        ___________________
        """
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point2.x,
            self.__point2.y,
            fill=fill_color,
            width=2
        )

from window import Window
from cell import Cell
import time


class Maze:
    def __init__(
        self,
        x: int,
        y: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None
    ):
        """
        : @summary :
        Represents a maze of cells.
        ___________________

        : @args :
            * x (int): left coord
            * y (int): top coord
            * num_rows (int): the number of rows in the maze
            * num_cols (int): the number of columns in the maze
            * cell_size_x (int): the width of cells
            * cell_size_y (int): the height of cells
            * win (Window): the window to render in
        ___________________
        """
        self.__x = x
        self.__y = y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.cells = []
        self.create_cells()

    def create_cells(self):
        """
        : @summary :
        Fills the cells of the maze.
        ___________________
        """
        # populate the cells
        for i in range(self.__num_rows):
            row = []
            for j in range(self.__num_cols):
                x1 = self.__x + self.__cell_size_x * i
                y1 = self.__y + self.__cell_size_y * j
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y
                new_cell = Cell(x1, y1, x2, y2, self.__win)
                row.append(new_cell)
            self.cells.append(row)
            
        if self.__win is None:
            return
        
        # draw and animate the cells
        for row in self.cells:
            for cell in row:
                cell.draw()
                
        self.__break_entrance_and_exit()

    def __animate(self):
        """
        : @summary :
        Animate the maze for a frame, then sleep.
        ___________________
        """
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        """
        : @summary :
        Removes the top of the top-left cell and the bottom of the bottom-right cell.
        ___________________
        """
        top_left = self.cells[0][0]
        top_left.has_top_wall = False
        top_left.draw()
        
        bottom_right = self.cells[-1][-1]
        bottom_right.has_bottom_wall = False
        bottom_right.draw()
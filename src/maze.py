from window import Window
from cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x: int,
        y: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None,
        seed: int = None,
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
            * seed (int): a seed for deterministic testing
        ___________________
        """
        self.__x = x
        self.__y = y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        if seed is not None:
            random.seed(seed)

        self.cells = []
        self.create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls(0, 0)
        self.__reset_cells_visited()

    def solve(self):
        """
        : @summary :
        Solves the maze.
        ___________________
        """
        return self.__solve_rec(0, 0)

    def __solve_rec(self, i, j):
        self.__animate()

        # vist the current cell
        self.cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self.cells[i][j].has_left_wall
            and not self.cells[i - 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i - 1][j])
            if self.__solve_rec(i - 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self.__num_cols - 1
            and not self.cells[i][j].has_right_wall
            and not self.cells[i + 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self.__solve_rec(i + 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self.cells[i][j].has_top_wall
            and not self.cells[i][j - 1].visited
        ):
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self.__solve_rec(i, j - 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self.__num_rows - 1
            and not self.cells[i][j].has_bottom_wall
            and not self.cells[i][j + 1].visited
        ):
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self.__solve_rec(i, j + 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False

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
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int):
        """
        : @summary :
        Draws a cell on the canvas.
        ___________________

        : @args :
            * i (int): the row of the cell to draw
            * j (int): the col of the cell to draw
        ___________________
        """
        if self.__win is None:
            return
        self.cells[i][j].draw()
        self.__win.redraw()

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
        self.__draw_cell(0, 0)

        bottom_right = self.cells[-1][-1]
        bottom_right.has_bottom_wall = False
        self.__draw_cell(-1, -1)

    def __break_walls(self, i: int, j: int):
        """
        : @summary :
        A recursive method that uses Depth-First Search (DFS) to randomly
        break walls (based on the seed) to create a maze.
        ___________________

        : @args :
            * i (int): cell row
            * j (int): cell col
        ___________________
        """
        self.cells[i][j].visited = True  # mark current cell as visited

        while True:
            to_visit = []

            # determine which cell(s) to visit next
            if i > 0 and not self.cells[i - 1][j].visited:  # left
                to_visit.append((i - 1, j))
            # right
            if i < self.__num_cols - 1 and not self.cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self.cells[i][j - 1].visited:  # up
                to_visit.append((i, j - 1))
            # down
            if j < self.__num_rows - 1 and not self.cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            # if there is nowhere to go from here just break out
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]

            # knock out walls between this cell and the next cell(s)
            if next_index[0] == i + 1:  # right
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:  # left
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:  # down
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:  # up
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self.__break_walls(next_index[0], next_index[1])

    def __reset_cells_visited(self):
        """
        : @summary :
        Resets all cells to unvisited.
        ___________________
        """
        for row in self.cells:
            for cell in row:
                cell.visited = False

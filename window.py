from tkinter import Tk, BOTH, Canvas
from typing import Self


class Window:
    def __init__(self: Self, width: int, height: int) -> None:
        """
        : @summary :
        Represents the main GUI window.
        ___________________

        : @args :
            * width (int): window width
            * height (int): window height
        ___________________
        """
        # members
        self.__root = Tk()
        self.__canvas = Canvas(self.__root, bg="white",
                               width=width, height=height)
        self.__running = False

        # other initialisation
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)  # binds close
        self.__canvas.pack(fill=BOTH, expand=1)

    def redraw(self: Self) -> None:
        """
        : @summary :
        Redraws the canvas.
        ___________________
        """
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self: Self) -> None:
        """
        : @summary :
        The main render loop. Redraws whilst the window is running.
        ___________________
        """
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self: Self) -> None:
        """
        : @summary :
        Ends the main loop.
        ___________________
        """
        print("Closing window...")
        self.__running = False

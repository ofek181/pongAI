from abc import ABC, abstractmethod


class Position(ABC):
    """
        A class for implementing x,y position on the screen
        ----------------------------
        Attributes
        ----------------------------
        x_pos
            x position on the screen
        y_pos
            y position on the screen
        ----------------------------
        Methods
        ----------------------------
        __init__(self, x_pos, y_pos):
            Constructs all the necessary attributes for the Position object.
        set_pos(self):
            abstract method for setting the attributes
    """
    def __init__(self, x_pos: int, y_pos: int):
        """
            Constructs all the necessary attributes for the Position object.
        """
        self.x_pos = x_pos
        self.y_pos = y_pos

    @abstractmethod
    def _set_position(self, x_pos: int, y_pos: int):
        """
            Abstract method for setting position to later be implemented.
        """
        pass

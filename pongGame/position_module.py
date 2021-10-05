from abc import ABC, abstractmethod


class Position(metaclass=ABC):
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
        __init__(self):
            Constructs all the necessary attributes for the Position object.
        set_pos(self):
            abstract method for setting the attributes
    """
    def __init__(self):
        """
            Constructs all the necessary attributes for the Position object.
        """
        self.x_pos = 0
        self.y_pos = 0

    @abstractmethod
    def set_pos(self):
        """
            Abstract method for setting position to later be implemented.
        """
        pass

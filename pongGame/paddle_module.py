from .consts_file import PaddleConsts
from .position_module import Position
from .velocity_module import Velocity


class Paddle(Position, Velocity):
    """
        A class to implement the Paddle object.
        ----------------------------
        Attributes
        ----------------------------
        m_size: [int, int]
         defines paddle size on the x and y axis.
        ----------------------------
        Methods
        ----------------------------
        __init__(self):
         Constructs all the necessary attributes for the Paddle object.
        __set_position(self):
         sets the initial Position of the Paddle.
        __set_velocity(self):
         sets the initial Velocity of the Paddle.
        __set_size(self):
         sets the size of the Paddle.
        move(self):
         Calculates the next position of the Paddle based on its velocity.
    """
    def __init__(self, x_pos: int = 900, y_pos: int = 300):
        """
            Constructs all the necessary attributes for the Paddle object.
        """
        Position.__init__(self, x_pos=x_pos, y_pos=y_pos)
        Velocity.__init__(self, x_vel=0, y_vel=0)
        self.__set_size()

    def move(self):
        """
            Implements the movement of the Paddle object.
        """
        self.x_pos = self.x_pos + self.x_vel
        self.y_pos = self.y_pos + self.y_vel

    def _set_position(self, x_pos: int, y_pos: int):
        """
            Sets Position of the Paddle object.
        """
        self.x_pos = x_pos
        self.y_pos = y_pos

    def _set_velocity(self, x_vel: int, y_vel: int):
        """
            Sets Velocity of the Paddle object.
        """
        self.x_vel = x_vel
        self.y_vel = y_vel

    def __set_size(self):
        """
            Sets size of the Paddle object.
        """
        self.m_size = PaddleConsts.PADDLE_SIZE



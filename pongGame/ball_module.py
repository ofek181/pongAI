from .consts_file import BallConsts
from .position_module import Position
from .velocity_module import Velocity


class Ball(Position, Velocity):
    """
        A class to implement the Ball object.
        ----------------------------
        Attributes
        ----------------------------
        m_radius: int
         defines ball radius and therefore its size.
        ----------------------------
        Methods
        ----------------------------
        __init__(self):
         Constructs all the necessary attributes for the Ball object.
        __set_position(self):
         sets the initial Position of the ball.
        __set_velocity(self):
         sets the initial Velocity of the ball.
        __set_radius(self):
         sets the radius of the ball.
        move(self):
         Calculates the next position of the ball based on its velocity.
    """
    def __init__(self):
        """
            Constructs all the necessary attributes for the Ball object.
        """
        Position.__init__(self, BallConsts.BALL_STARTING_POSITION_X,
                          BallConsts.BALL_STARTING_POSITION_Y)
        Velocity.__init__(self, BallConsts.BALL_STARTING_VELOCITY_X,
                          BallConsts.BALL_STARTING_VELOCITY_Y)
        self.__set_radius()

    def _set_position(self, x_pos: int, y_pos: int):
        """
            Sets Position of the Ball object.
        """
        self.x_pos = x_pos
        self.y_pos = y_pos

    def _set_velocity(self, x_vel: int, y_vel: int):
        """
            Sets Velocity of the Ball object.
        """
        self.x_vel = x_vel
        self.y_vel = y_vel

    def __set_radius(self):
        """
            Sets radius of the Ball object.
        """
        self.m_radius = BallConsts.BALL_RADIUS

    def move(self):
        """
            Implements the movement of the Ball object.
        """
        self.x_pos = self.x_pos + self.x_vel
        self.y_pos = self.y_pos + self.y_vel



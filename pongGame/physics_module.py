from .position_module import Position
from .velocity_module import Velocity
from .ball_module import Ball
from .paddle_module import Paddle


class Physics:
    """
        A static class to implement the physics of the game.
        ----------------------------
        Methods
        ----------------------------
        calc_ball_velocity(ball: Ball, paddle: Paddle) -> Velocity:
         Calculates the velocity of the ball for the following frame.
        calc_next_ball_position(ball: Ball, paddle: Paddle) -> Position:
         Calculates the position of the ball for the following frame.
        calc_next_paddle_position(paddle: Paddle) -> Position:
         Calculates the position of the paddle for the following frame.
        calc_ball_paddle_intersection(ball: Ball, paddle: Paddle) -> Position:
         Calculates the intersection of the ball with the paddle.
    """

    @staticmethod
    def calc_ball_velocity(ball: Ball, paddle: Paddle) -> Velocity:
        """
            Calculates the velocity of the ball for the following frame.
        """
        pass

    @staticmethod
    def calc_next_ball_position(ball: Ball, paddle: Paddle) -> Position:
        """
            Calculates the position of the ball for the following frame.
        """
        pass

    @staticmethod
    def calc_next_paddle_position(paddle: Paddle) -> Position:
        """
            Calculates the position of the paddle for the following frame.
        """
        pass

    @staticmethod
    def calc_ball_paddle_intersection(ball: Ball, paddle: Paddle) -> Position:
        """
            Calculates the intersection of the ball with the paddle.
        """
        pass


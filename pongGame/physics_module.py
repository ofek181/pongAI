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
    def ball_paddle_intersection(ball: Ball, paddle: Paddle) -> [bool, int, str]:
        """
            Calculates the intersection of the ball with the paddle.
            Returns:
                collision: whether or not a collision occurred.
                dist: collision distance between the ball and paddle on the y_axis.
                section: section of the paddle in which the collision occurred.
        """
        collision = False
        dist = 0
        section = "None"

        if ball.x_pos + ball.m_radius == paddle.x_pos - paddle.m_size[0]:  # right paddle intersection
            collision = True
        if ball.x_pos - ball.m_radius == paddle.x_pos + paddle.m_size[0]:  # left paddle intersection
            collision = True
        if collision:
            ball_center = [ball.x_pos, ball.y_pos]
            paddle_center = [paddle.x_pos + paddle.m_size[0] / 2,
                             paddle.y_pos + paddle.m_size[1] / 2]
            if ball_center[1] <= paddle_center[1]:  # ball is on the top side of the paddle
                dist = paddle_center[1] - ball_center[1]
                section = "TOP"

            else:  # ball is on the bottom side of the paddle
                dist = ball_center[1] - paddle_center[1]
                section = "BOT"

        return collision, dist, section



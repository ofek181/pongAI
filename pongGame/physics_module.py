import math
from .velocity_module import Velocity
from .ball_module import Ball
from .paddle_module import Paddle
from consts_file import DisplayConsts


class Physics:
    """
        A static class to implement the physics of the game.
        ----------------------------
        Methods
        ----------------------------
        calc_ball_velocity(ball: Ball, paddle: Paddle) -> Velocity:
         Calculates the velocity of the ball for the following frame.
        ball_screen_intersection(ball: Ball) -> bool:
         Checks whether an intersection of the ball with the screen occurred.
        ball_paddle_intersection(ball: Ball, paddle: Paddle) -> [bool, int]:
         Calculates the intersection of the ball with the paddle.
    """

    def calc_ball_velocity(self, ball: Ball, paddle: Paddle) -> Velocity:
        """
            Calculates the velocity of the ball for the following frame.
        """
        vel = Velocity(ball.x_vel, ball.y_vel)

        if self.ball_paddle_intersection(ball, paddle)[0]:
            bounce_angle = self.ball_paddle_intersection(ball, paddle)[1] * 90
            ball_speed = math.sqrt(ball.x_vel**2 + ball.y_vel**2)
            new_x_vel = -ball_speed * math.cos(bounce_angle)
            new_y_vel = ball_speed * math.sin(bounce_angle)
            vel = Velocity(new_x_vel, new_y_vel)

        if self.ball_screen_intersection(ball):
            new_y_vel = -ball.y_vel
            vel = Velocity(ball.x_vel, new_y_vel)

        return vel

    @staticmethod
    def ball_screen_intersection(ball: Ball) -> bool:
        if ball.y_pos - ball.m_radius == 0 or ball.y_pos + ball.m_radius == DisplayConsts.SCREEN_HEIGHT:
            return True
        return False

    @staticmethod
    def ball_paddle_intersection(ball: Ball, paddle: Paddle) -> [bool, float]:
        """
            Calculates the intersection of the ball with the paddle.
            Returns:
                collision: whether or not a collision occurred.
                dist: collision distance between the ball and paddle on the y_axis.
        """
        collision = False
        normalized_dist = 0

        if ball.x_pos + ball.m_radius == paddle.x_pos - paddle.m_size[0]:  # right paddle intersection
            collision = True
        if ball.x_pos - ball.m_radius == paddle.x_pos + paddle.m_size[0]:  # left paddle intersection
            collision = True
        if collision:
            # dist is positive if the ball is on the bottom of the paddle
            normalized_dist = (ball.y_pos - (paddle.y_pos + paddle.m_size[1] / 2)) / paddle.m_size[1]

            if abs(normalized_dist) > 1/2:
                raise Exception("Distance during intersection Error")

        return collision, normalized_dist



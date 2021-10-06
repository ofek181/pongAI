import math
from .velocity_module import Velocity
from .ball_module import Ball
from .paddle_module import Paddle
from .audio_module import Audio
from .consts_file import DisplayConsts, BallConsts


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
        ball_paddle_intersection(ball: Ball, paddle: Paddle) -> [bool, bool, int]:
         Calculates the intersection of the ball with the paddle.
        is_score(ball: Ball) -> [bool, bool]
         returns a tuple of bool depending on which paddle scored
    """

    @staticmethod
    def calc_ball_velocity(ball: Ball, paddle_left: Paddle, paddle_right: Paddle) -> Velocity:
        """
            Calculates the velocity of the ball for the following frame.
        """
        acceleration = 0.2
        vel = Velocity(ball.x_vel, ball.y_vel)

        # intersection with the left paddle
        if Physics.__ball_paddle_intersection(ball, paddle_left, paddle_right)[0]:
            angle = Physics.__ball_paddle_intersection(ball, paddle_left, paddle_right)[2] * 90
            bounce = math.copysign(abs(min([angle, BallConsts.MAX_BOUNCE_ANGLE], key=abs)), angle)
            ball_speed = math.sqrt(ball.x_vel**2 + ball.y_vel**2) + acceleration  # make the ball accelerate
            x_vel = ball_speed * math.cos(math.degrees(bounce))
            new_x_vel = max([x_vel, BallConsts.MIN_X_VEL], key=abs)
            new_y_vel = ball_speed * math.sin(math.degrees(bounce))
            vel = Velocity(new_x_vel, new_y_vel)  # make ball accelerate each intersection
            Audio.sound_hit()

        # intersection with the right paddle
        if Physics.__ball_paddle_intersection(ball, paddle_left, paddle_right)[1]:
            angle = Physics.__ball_paddle_intersection(ball, paddle_left, paddle_right)[2] * 90
            bounce = math.copysign(abs(min([angle, BallConsts.MAX_BOUNCE_ANGLE], key=abs)), angle)
            ball_speed = math.sqrt(ball.x_vel ** 2 + ball.y_vel ** 2) + acceleration
            x_vel = -ball_speed * math.cos(math.degrees(bounce))
            new_x_vel = max([x_vel, -BallConsts.MIN_X_VEL], key=abs)
            new_y_vel = ball_speed * math.sin(math.degrees(bounce))
            vel = Velocity(new_x_vel, new_y_vel)  # make ball accelerate each intersection
            Audio.sound_hit()

        # intersection with the screen
        if Physics.__ball_screen_intersection(ball):
            new_y_vel = -ball.y_vel
            vel = Velocity(ball.x_vel, new_y_vel)

        return vel

    @staticmethod
    def __ball_screen_intersection(ball: Ball) -> bool:
        if ball.y_pos - ball.m_radius <= 0 or ball.y_pos + ball.m_radius >= DisplayConsts.SCREEN_HEIGHT:
            return True
        return False

    @staticmethod
    def __ball_paddle_intersection(ball: Ball, paddle_left: Paddle, paddle_right: Paddle) -> [bool, bool, float]:
        """
            Calculates the intersection of the ball with the paddle.
            Returns:
                collision: whether or not a collision occurred.
                dist: collision distance between the ball and paddle on the y_axis.
        """
        collision_right = False
        collision_left = False
        normalized_dist = 0
        buffer = 5

        # right paddle intersection
        if paddle_right.x_pos+paddle_right.m_size[0]+buffer >= ball.x_pos+ball.m_radius >= paddle_right.x_pos-buffer:
            if ball.x_vel > 0:
                if paddle_right.y_pos <= ball.y_pos <= paddle_right.y_pos + paddle_right.m_size[1]:
                    collision_right = True
                    normalized_dist = (paddle_right.y_pos + paddle_right.m_size[1] / 2
                                       - ball.y_pos) / paddle_right.m_size[1]

        # left paddle intersection
        if paddle_left.x_pos-buffer <= ball.x_pos - ball.m_radius <= paddle_left.x_pos+paddle_left.m_size[0]+buffer:
            if ball.x_vel < 0:
                if paddle_left.y_pos <= ball.y_pos <= paddle_left.y_pos + paddle_left.m_size[1]:
                    collision_left = True
                    normalized_dist = (paddle_left.y_pos + paddle_left.m_size[1] / 2
                                       - ball.y_pos) / paddle_left.m_size[1]

        if abs(normalized_dist) > 1/2:
            raise Exception("Distance during intersection Error")

        if collision_right or collision_left:
            print(normalized_dist)

        return collision_left, collision_right, normalized_dist

    @staticmethod
    def is_score(ball: Ball) -> [bool, bool]:
        """
           Checks if a goal occurred
           Returns:
               return a tuple of bool depending on who scored.
       """
        if ball.x_pos >= DisplayConsts.SCREEN_WIDTH:
            Audio.sound_score()
            return [True, False]
        if ball.x_pos <= 0:
            Audio.sound_score()
            return [False, True]

        return [False, False]



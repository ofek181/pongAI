import pygame
from .game_interface import Game
from .ball_module import Ball
from .paddle_module import Paddle
from .event_handler_module import EventHandler
from .physics_module import Physics
from .display_module import Display
from .consts_file import GameConsts, DisplayConsts, Action
global run


class Pong(Game):
    """
        A class to implement the Pong game.
        ----------------------------
        Attributes
        ----------------------------
        m_paddle_left: Paddle
         the left side paddle.
        m_paddle_right: Paddle
        the right side paddle.
        m_ball: Ball
         ball of the game.
        paddle_left_score: int
         left player score.
        paddle_right_score: int
         right player score.
        display : Display
         display for the game.
        ----------------------------
        Methods
        ----------------------------
        __init__(self):
         Constructs all the necessary attributes for the Pong object.
        _is_game_over(self) -> bool:
         checks whether the game is over based on MAX SCORE.
        _calc_frame(self):
         calculates a single frame of the game.
        run_game(self):
         main loop of the game.
    """
    def __init__(self):
        """
            Constructs all the necessary attributes for the Pong object.
        """
        self.m_paddle_left = Paddle(x_pos=50, y_pos=DisplayConsts.SCREEN_HEIGHT//2)
        self.m_paddle_right = Paddle(x_pos=DisplayConsts.SCREEN_WIDTH-50,
                                     y_pos=DisplayConsts.SCREEN_HEIGHT//2)
        self.m_ball = Ball()
        self.paddle_left_score = 0
        self.paddle_right_score = 0
        self.display = Display()

    def _is_game_over(self) -> bool:
        """
             Checks for game over state based on MAX_SCORE.
        """
        if self.paddle_left_score == GameConsts.MAX_SCORE or self.paddle_right_score == GameConsts.MAX_SCORE:
            return True
        return False

    def _calc_frame(self):
        """
             Calculates a single frame of the game.
        """
        global run
        # get actions for both players
        action_left = EventHandler.handle_left_events()
        action_right = EventHandler.handle_right_events()

        # move the paddles
        if action_left == Action.MOVE_UP:
            self.m_paddle_left.move(-self.m_paddle_left.y_vel)
        if action_left == Action.MOVE_DOWN:
            self.m_paddle_left.move(self.m_paddle_left.y_vel)
        if action_right == Action.MOVE_UP:
            self.m_paddle_right.move(-self.m_paddle_right.y_vel)
        if action_right == Action.MOVE_DOWN:
            self.m_paddle_right.move(self.m_paddle_right.y_vel)
        # quit the game if needed
        if (action_right or action_left) == Action.QUIT:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            run = False

        # move the ball
        self.m_ball.move()

        # check for intersections
        left_vel = Physics.calc_ball_velocity(self.m_ball, self.m_paddle_left)
        right_vel = Physics.calc_ball_velocity(self.m_ball, self.m_paddle_right)

        # if an intersection occurred
        if [left_vel.x_vel, left_vel.y_vel] != [self.m_ball.x_vel, self.m_ball.y_vel]:
            self.m_ball.x_vel, self.m_ball.y_vel = left_vel.x_vel, left_vel.y_vel
        if [right_vel.x_vel, right_vel.y_vel] != [self.m_ball.x_vel, self.m_ball.y_vel]:
            self.m_ball.x_vel, self.m_ball.y_vel = right_vel.x_vel, right_vel.y_vel

        # TODO implement the scoring system
        # TODO check why quit doesnt work
        # TODO fix the physics class
        # TODO add all consts to constfile

    def run_game(self):
        """
             Main loop of the game.
        """
        global run
        run = True
        while run:
            self.display.animate_game(paddle_left=self.m_paddle_left,
                                      paddle_right=self.m_paddle_right,
                                      ball=self.m_ball)
            self.display.show_score(score_left=self.paddle_left_score,
                                    score_right=self.paddle_right_score)
            if self.paddle_left_score == GameConsts.MAX_SCORE:
                self.display.show_winner("Left Player Wins!")
            if self.paddle_right_score == GameConsts.MAX_SCORE:
                self.display.show_winner("Right Player Wins!")
            self._calc_frame()


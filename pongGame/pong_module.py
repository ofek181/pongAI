from .game_interface import Game
from .ball_module import Ball
from .paddle_module import Paddle
from .consts_file import GameConsts, DisplayConsts


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
        pass

    def run_game(self):
        """
             Main loop of the game.
        """
        pass

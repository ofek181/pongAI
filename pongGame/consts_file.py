import os
from enum import Enum
local_dir_audio = os.path.join(os.path.dirname(__file__), "audio")


class DisplayConsts:
    FPS = 30
    SCREEN_WIDTH = 950
    SCREEN_HEIGHT = 550
    FONT_COLOR = (255, 255, 255)
    LINE_FONT = (50, 50, 50)
    LINE_WIDTH = 10
    FONT_SIZE = 80
    WINNER_SIZE = 130
    FONT_TYPE = 'Comic Sans MS'


class AudioConsts:
    GAME_OVER_AUDIO = os.path.join(local_dir_audio, 'game_over.wav')
    SCORE_AUDIO = os.path.join(local_dir_audio, 'score.wav')


class BallConsts:
    BALL_RADIUS = 10
    BALL_STARTING_POSITION_X = 100
    BALL_STARTING_POSITION_Y = 200
    BALL_STARTING_VELOCITY_X = 10
    BALL_STARTING_VELOCITY_Y = 0


class PaddleConsts:
    PADDLE_SIZE = [10, 60]


class Action(Enum):
    NO_ACTION = 0
    LEFT_PADDLE_MOVE_UP = 1
    LEFT_PADDLE_MOVE_DOWN = 2
    RIGHT_PADDLE_MOVE_UP = 3
    RIGHT_PADDLE_MOVE_DOWN = 4
    QUIT = 5





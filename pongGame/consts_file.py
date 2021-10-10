import os
from enum import Enum
local_dir_audio = os.path.join(os.path.dirname(__file__), "audio")


class DisplayConsts:
    FPS = 144
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400
    FONT_COLOR = (255, 255, 255)
    LINE_FONT = (50, 50, 50)
    LINE_WIDTH = 10
    FONT_SIZE = 80
    WINNER_SIZE = 90
    FONT_TYPE = '8-Bit-Madness'


class AudioConsts:
    HIT_AUDIO = os.path.join(local_dir_audio, 'hit.wav')
    SCORE_AUDIO = os.path.join(local_dir_audio, 'score.wav')


class BallConsts:
    BALL_RADIUS = 10
    BALL_STARTING_POSITION_X = DisplayConsts.SCREEN_WIDTH // 2
    BALL_STARTING_POSITION_Y = DisplayConsts.SCREEN_HEIGHT // 2
    BALL_STARTING_VELOCITY_X = 3
    BALL_STARTING_VELOCITY_Y = 0
    MIN_X_VEL = BALL_STARTING_VELOCITY_X
    MAX_BOUNCE_ANGLE = 70
    ACCELERATION = 0.2


class PaddleConsts:
    PADDLE_SIZE = [10, 70]
    PADDLE_VELOCITY = 3


class GameConsts:
    MAX_SCORE = 5


class Action(Enum):
    NO_ACTION = 0
    MOVE_UP = 1
    MOVE_DOWN = 2
    QUIT = 9




